"""
Script to create formatted Excel traceability matrix with summary statistics
"""

import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_traceability_excel(csv_file, excel_file):
    """Create formatted Excel traceability matrix"""
    wb = Workbook()
    
    # Remove default sheet
    wb.remove(wb.active)
    
    # Create Requirements to Test Cases sheet
    ws1 = wb.create_sheet("Requirements to Test Cases", 0)
    
    # Create Summary sheet
    ws2 = wb.create_sheet("Summary", 1)
    
    # Define styles
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    req_fill = PatternFill(start_color="E7F3FF", end_color="E7F3FF", fill_type="solid")
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Read CSV and write to Excel
    requirements = []
    test_case_ids = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        test_case_ids = header[3:]  # Get test case IDs from header
        
        # Write header
        for col_idx, value in enumerate(header, start=1):
            cell = ws1.cell(row=1, column=col_idx, value=value)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.border = border
        
        # Write data rows
        for row_idx, row in enumerate(reader, start=2):
            if not row or len(row) < 3:  # Skip empty rows
                continue
            req_id = row[0]
            req_name = row[1]
            req_desc = row[2]
            coverage = row[3:] if len(row) > 3 else []
            
            # Pad coverage to match test case count
            while len(coverage) < len(test_case_ids):
                coverage.append('')
            
            requirements.append({
                'id': req_id,
                'name': req_name,
                'description': req_desc,
                'coverage': coverage[:len(test_case_ids)]  # Ensure exact match
            })
            
            # Write requirement info
            for col_idx in range(1, 4):
                cell = ws1.cell(row=row_idx, column=col_idx, value=row[col_idx-1])
                cell.fill = req_fill
                cell.font = Font(bold=True)
                cell.border = border
                cell.alignment = Alignment(vertical='top', wrap_text=True)
            
            # Write coverage (X marks)
            for col_idx, value in enumerate(coverage[:len(test_case_ids)], start=4):
                cell = ws1.cell(row=row_idx, column=col_idx, value=value)
                cell.border = border
                cell.alignment = Alignment(horizontal='center', vertical='center')
                if value == 'X':
                    cell.fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
    
    # Set column widths
    ws1.column_dimensions['A'].width = 12  # Requirement ID
    ws1.column_dimensions['B'].width = 35  # Feature/Requirement
    ws1.column_dimensions['C'].width = 50  # Description
    for col_idx in range(4, ws1.max_column + 1):
        ws1.column_dimensions[get_column_letter(col_idx)].width = 8  # Test case columns
    
    # Freeze first 3 columns
    ws1.freeze_panes = 'D2'
    
    # Create Summary Sheet
    ws2['A1'] = 'Traceability Matrix Summary'
    ws2['A1'].font = Font(bold=True, size=16)
    
    # Calculate statistics
    total_requirements = len(requirements)
    total_test_cases = len(test_case_ids)
    
    # Count coverage per requirement
    req_coverage = []
    for req in requirements:
        covered = sum(1 for x in req['coverage'] if x == 'X')
        coverage_pct = (covered / total_test_cases) * 100 if total_test_cases > 0 else 0
        req_coverage.append({
            'req_id': req['id'],
            'req_name': req['name'],
            'covered': covered,
            'total': total_test_cases,
            'coverage_pct': coverage_pct
        })
    
    # Count requirements per test case
    tc_coverage = []
    for tc_idx, tc_id in enumerate(test_case_ids):
        covered = sum(1 for req in requirements if req['coverage'][tc_idx] == 'X')
        coverage_pct = (covered / total_requirements) * 100 if total_requirements > 0 else 0
        tc_coverage.append({
            'tc_id': tc_id,
            'covered': covered,
            'total': total_requirements,
            'coverage_pct': coverage_pct
        })
    
    # Write summary statistics
    row = 3
    ws2[f'A{row}'] = 'Overall Statistics'
    ws2[f'A{row}'].font = Font(bold=True, size=12)
    row += 1
    
    ws2[f'A{row}'] = 'Total Requirements:'
    ws2[f'B{row}'] = total_requirements
    row += 1
    
    ws2[f'A{row}'] = 'Total Test Cases:'
    ws2[f'B{row}'] = total_test_cases
    row += 1
    
    avg_coverage = sum(r['coverage_pct'] for r in req_coverage) / len(req_coverage) if req_coverage else 0
    ws2[f'A{row}'] = 'Average Requirement Coverage:'
    ws2[f'B{row}'] = f"{avg_coverage:.2f}%"
    row += 2
    
    # Requirements Coverage Table
    ws2[f'A{row}'] = 'Requirements Coverage'
    ws2[f'A{row}'].font = Font(bold=True, size=12)
    row += 1
    
    # Header
    headers = ['Requirement ID', 'Requirement Name', 'Test Cases Covered', 'Total Test Cases', 'Coverage %']
    for col_idx, header in enumerate(headers, start=1):
        cell = ws2.cell(row=row, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.border = border
        cell.alignment = Alignment(horizontal='center', vertical='center')
    row += 1
    
    # Data rows
    for req_cov in sorted(req_coverage, key=lambda x: x['coverage_pct'], reverse=True):
        ws2.cell(row=row, column=1, value=req_cov['req_id']).border = border
        ws2.cell(row=row, column=2, value=req_cov['req_name']).border = border
        ws2.cell(row=row, column=3, value=req_cov['covered']).border = border
        ws2.cell(row=row, column=4, value=req_cov['total']).border = border
        cell = ws2.cell(row=row, column=5, value=f"{req_cov['coverage_pct']:.2f}%")
        cell.border = border
        
        # Color code coverage
        if req_cov['coverage_pct'] >= 80:
            cell.fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
        elif req_cov['coverage_pct'] >= 50:
            cell.fill = PatternFill(start_color="FFE4B5", end_color="FFE4B5", fill_type="solid")
        else:
            cell.fill = PatternFill(start_color="FFB6C1", end_color="FFB6C1", fill_type="solid")
        
        row += 1
    
    row += 2
    
    # Test Cases Coverage Table
    ws2[f'A{row}'] = 'Test Cases Coverage'
    ws2[f'A{row}'].font = Font(bold=True, size=12)
    row += 1
    
    # Header
    headers = ['Test Case ID', 'Requirements Covered', 'Total Requirements', 'Coverage %']
    for col_idx, header in enumerate(headers, start=1):
        cell = ws2.cell(row=row, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.border = border
        cell.alignment = Alignment(horizontal='center', vertical='center')
    row += 1
    
    # Data rows (show top 20)
    for tc_cov in sorted(tc_coverage, key=lambda x: x['covered'], reverse=True)[:20]:
        ws2.cell(row=row, column=1, value=tc_cov['tc_id']).border = border
        ws2.cell(row=row, column=2, value=tc_cov['covered']).border = border
        ws2.cell(row=row, column=3, value=tc_cov['total']).border = border
        cell = ws2.cell(row=row, column=4, value=f"{tc_cov['coverage_pct']:.2f}%")
        cell.border = border
        
        # Color code coverage
        if tc_cov['coverage_pct'] >= 30:
            cell.fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
        elif tc_cov['coverage_pct'] >= 15:
            cell.fill = PatternFill(start_color="FFE4B5", end_color="FFE4B5", fill_type="solid")
        else:
            cell.fill = PatternFill(start_color="FFB6C1", end_color="FFB6C1", fill_type="solid")
        
        row += 1
    
    # Set column widths for summary
    ws2.column_dimensions['A'].width = 30
    ws2.column_dimensions['B'].width = 20
    ws2.column_dimensions['C'].width = 20
    ws2.column_dimensions['D'].width = 20
    ws2.column_dimensions['E'].width = 15
    
    # Save file
    wb.save(excel_file)
    print(f"Traceability matrix Excel created: {excel_file}")
    print(f"Total Requirements: {total_requirements}")
    print(f"Total Test Cases: {total_test_cases}")
    print(f"Average Coverage: {avg_coverage:.2f}%")

if __name__ == "__main__":
    csv_file = 'traceability_matrix.csv'
    excel_file = 'traceability_matrix.xlsx'
    
    try:
        create_traceability_excel(csv_file, excel_file)
        print("Conversion completed successfully!")
    except FileNotFoundError:
        print(f"Error: {csv_file} not found!")
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

