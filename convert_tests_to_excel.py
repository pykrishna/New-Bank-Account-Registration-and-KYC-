"""
Script to convert functional_test_cases.csv to formatted Excel file
Run this script to generate functional_test_cases.xlsx
"""

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def format_excel_file(file_path):
    """Format the Excel file with colors and styling"""
    wb = load_workbook(file_path)
    ws = wb.active
    
    # Define styles
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Format header row
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = border
    
    # Format data rows
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        for cell in row:
            cell.border = border
            cell.alignment = Alignment(vertical='top', wrap_text=True)
            
            # Color code by priority
            if cell.column == 4:  # Priority column
                if cell.value == 'Critical':
                    cell.fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                    cell.font = Font(bold=True, color="FFFFFF")
                elif cell.value == 'High':
                    cell.fill = PatternFill(start_color="FF9900", end_color="FF9900", fill_type="solid")
                    cell.font = Font(bold=True, color="FFFFFF")
                elif cell.value == 'Medium':
                    cell.fill = PatternFill(start_color="FFCC00", end_color="FFCC00", fill_type="solid")
                elif cell.value == 'Low':
                    cell.fill = PatternFill(start_color="CCFFCC", end_color="CCFFCC", fill_type="solid")
            
            # Color code by status
            if cell.column == 9:  # Status column
                if cell.value == 'Pass':
                    cell.fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
                elif cell.value == 'Fail':
                    cell.fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                    cell.font = Font(bold=True, color="FFFFFF")
                elif cell.value == 'Pending':
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
    
    # Save formatted file
    wb.save(file_path)
    print(f"✅ Excel file formatted and saved: {file_path}")

def main():
    # Read CSV file
    csv_file = 'functional_test_cases.csv'
    excel_file = 'functional_test_cases.xlsx'
    
    try:
        # Read CSV
        df = pd.read_csv(csv_file)
        
        # Write to Excel
        df.to_excel(excel_file, index=False, sheet_name='Test Cases')
        
        print(f"✅ CSV converted to Excel: {excel_file}")
        
        # Format Excel file
        format_excel_file(excel_file)
        
        print(f"\n📊 Test Cases Summary:")
        print(f"   Total Test Cases: {len(df)}")
        print(f"   By Priority:")
        print(df['Priority'].value_counts().to_string())
        print(f"\n   By Module:")
        print(df['Module'].value_counts().to_string())
        
    except FileNotFoundError:
        print(f"❌ Error: {csv_file} not found!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()


