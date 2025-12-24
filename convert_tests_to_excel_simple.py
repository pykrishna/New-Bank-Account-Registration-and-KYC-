"""
Simple script to convert functional_test_cases.csv to formatted Excel file
Uses openpyxl directly (no pandas dependency)
"""

import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

def create_excel_from_csv(csv_file, excel_file):
    """Create formatted Excel file from CSV"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Cases"
    
    # Define styles
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Read CSV and write to Excel
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, start=1):
            for col_idx, value in enumerate(row, start=1):
                cell = ws.cell(row=row_idx, column=col_idx, value=value)
                cell.border = border
                
                # Format header row
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font
                    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                else:
                    cell.alignment = Alignment(vertical='top', wrap_text=True)
                    
                    # Color code by priority (column D)
                    if col_idx == 4:  # Priority column
                        if value == 'Critical':
                            cell.fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                            cell.font = Font(bold=True, color="FFFFFF")
                        elif value == 'High':
                            cell.fill = PatternFill(start_color="FF9900", end_color="FF9900", fill_type="solid")
                            cell.font = Font(bold=True, color="FFFFFF")
                        elif value == 'Medium':
                            cell.fill = PatternFill(start_color="FFCC00", end_color="FFCC00", fill_type="solid")
                        elif value == 'Low':
                            cell.fill = PatternFill(start_color="CCFFCC", end_color="CCFFCC", fill_type="solid")
                    
                    # Color code by status (column I)
                    if col_idx == 9:  # Status column
                        if value == 'Pass':
                            cell.fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
                        elif value == 'Fail':
                            cell.fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                            cell.font = Font(bold=True, color="FFFFFF")
                        elif value == 'Pending':
                            cell.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    
    # Auto-adjust column widths
    column_widths = {
        'A': 10,  # Test ID
        'B': 35,  # Test Case Name
        'C': 20,  # Module
        'D': 12,  # Priority
        'E': 30,  # Preconditions
        'F': 50,  # Test Steps
        'G': 40,  # Test Data
        'H': 50,  # Expected Result
        'I': 12,  # Status
        'J': 40   # Notes
    }
    
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width
    
    # Freeze header row
    ws.freeze_panes = 'A2'
    
    # Save file
    wb.save(excel_file)
    print(f"Excel file created: {excel_file}")

if __name__ == "__main__":
    csv_file = 'functional_test_cases.csv'
    excel_file = 'functional_test_cases.xlsx'
    
    try:
        create_excel_from_csv(csv_file, excel_file)
        print("Conversion completed successfully!")
    except FileNotFoundError:
        print(f"Error: {csv_file} not found!")
    except Exception as e:
        print(f"Error: {str(e)}")


