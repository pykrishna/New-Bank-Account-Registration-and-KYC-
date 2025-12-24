# 📋 Functional Test Scripts - User Guide

## 📁 Files Included

1. **functional_test_cases.csv** - Complete test case repository (90 test cases)
2. **test_execution_template.csv** - Template for tracking test execution
3. **convert_tests_to_excel.py** - Script to convert CSV to formatted Excel
4. **TEST_SCRIPTS_README.md** - This file

---

## 🚀 Quick Start

### Option 1: Use CSV Directly
1. Open `functional_test_cases.csv` in Excel, Google Sheets, or any CSV viewer
2. Filter and sort by Priority, Module, or Status
3. Use for test planning and execution

### Option 2: Convert to Excel (Recommended)
1. Run the conversion script:
   ```bash
   python convert_tests_to_excel.py
   ```
2. This creates `functional_test_cases.xlsx` with:
   - Color-coded priorities
   - Formatted headers
   - Auto-adjusted column widths
   - Status color coding

---

## 📊 Test Case Structure

Each test case includes:

| Column | Description |
|--------|-------------|
| **Test ID** | Unique identifier (TC001-TC090) |
| **Test Case Name** | Descriptive name |
| **Module** | Functional area (Registration, KYC Portal, AI Validation, etc.) |
| **Priority** | Critical, High, Medium, Low |
| **Preconditions** | What must be true before test |
| **Test Steps** | Step-by-step instructions |
| **Test Data** | Sample data to use |
| **Expected Result** | What should happen |
| **Status** | Pending, Pass, Fail, Blocked |
| **Notes** | Additional information |

---

## 🎯 Test Coverage

### By Module:
- **Registration** (6 test cases)
- **Authentication** (5 test cases)
- **KYC Portal** (17 test cases)
- **AI Validation** (14 test cases)
- **Status Check** (6 test cases)
- **Dashboard** (2 test cases)
- **Admin** (9 test cases)
- **Audit Reports** (4 test cases)
- **Validation** (8 test cases)
- **Error Handling** (3 test cases)
- **Performance** (2 test cases)
- **Security** (3 test cases)
- **Data Validation** (4 test cases)
- **Notifications** (2 test cases)
- **Data Integrity** (2 test cases)
- **Access Control** (2 test cases)
- **Reporting** (1 test case)

### By Priority:
- **Critical**: 15 test cases (Must pass for release)
- **High**: 35 test cases (Important functionality)
- **Medium**: 25 test cases (Standard functionality)
- **Low**: 15 test cases (Nice to have)

**Total: 90 Test Cases**

---

## 📝 Using Test Execution Template

1. **Open** `test_execution_template.csv`
2. **Fill in** execution details:
   - Executed By: Your name
   - Execution Date: Date of test
   - Execution Time: How long it took
   - Environment: Dev/Test/Staging/Prod
   - Status: Pass/Fail/Blocked/Skip
   - Actual Result: What actually happened
   - Defect ID: If test failed, link to bug
   - Comments: Any notes
   - Retest Status: If retesting after fix

3. **Track Progress**:
   - Filter by Status to see pass/fail rates
   - Filter by Executed By to see who tested what
   - Filter by Priority to focus on critical tests first

---

## 🎨 Excel Formatting Features

When you run `convert_tests_to_excel.py`, the Excel file includes:

### Color Coding:
- **Priority Column**:
  - 🔴 Critical: Red background
  - 🟠 High: Orange background
  - 🟡 Medium: Yellow background
  - 🟢 Low: Green background

- **Status Column**:
  - ✅ Pass: Green background
  - ❌ Fail: Red background with white text
  - ⏳ Pending: Yellow background

### Formatting:
- Bold headers with white text on blue background
- Borders on all cells
- Text wrapping for long content
- Auto-adjusted column widths
- Frozen header row (scrolls with data)

---

## 📋 Test Execution Workflow

### 1. **Test Planning Phase**
- Review all test cases
- Prioritize by Priority (Critical → High → Medium → Low)
- Assign test cases to team members
- Set up test environment

### 2. **Test Execution Phase**
- Open `test_execution_template.csv`
- Execute test cases one by one
- Record results:
  - ✅ Pass: Test passed as expected
  - ❌ Fail: Test failed, log defect
  - ⏸️ Blocked: Cannot execute (dependency issue)
  - ⏭️ Skip: Intentionally skipped

### 3. **Defect Tracking**
- For failed tests:
  - Create defect/bug report
  - Link defect ID in execution template
  - Add comments explaining failure

### 4. **Retest Phase**
- After fixes are implemented:
  - Retest failed test cases
  - Update Retest Status
  - Verify fixes

### 5. **Test Reporting**
- Generate summary:
  - Total tests: 90
  - Passed: X
  - Failed: Y
  - Blocked: Z
  - Pass Rate: (X/90) × 100%

---

## 🔍 Test Case Examples

### Example 1: Critical Test Case
**TC028 - KYC Validation - Face Matching Fail**
- **Priority**: Critical
- **Purpose**: Ensure system rejects when photo doesn't match ID
- **Steps**: Upload photo that doesn't match ID document photo
- **Expected**: Auto-rejection with critical issue flag

### Example 2: High Priority Test Case
**TC017 - PAN Card Upload - Valid Document**
- **Priority**: High
- **Purpose**: Verify PAN card processing works correctly
- **Steps**: Upload valid PAN card image
- **Expected**: OCR extracts PAN number and name, validation passes

### Example 3: Medium Priority Test Case
**TC020 - Document Upload - Blurry Image**
- **Priority**: Medium
- **Purpose**: Verify system handles poor quality images
- **Steps**: Upload blurry document
- **Expected**: Low OCR confidence, quality score deducted, may still pass

---

## 📊 Test Metrics

### Coverage Metrics:
- **Functional Coverage**: All major features covered
- **Priority Coverage**: 
  - Critical: 100% coverage
  - High: 95% coverage
  - Medium: 85% coverage
  - Low: 60% coverage

### Test Types:
- **Positive Tests**: Valid inputs, expected to pass
- **Negative Tests**: Invalid inputs, expected to fail gracefully
- **Boundary Tests**: Edge cases (file size limits, etc.)
- **Security Tests**: SQL injection, XSS, password hashing
- **Performance Tests**: Concurrent users, large files
- **Integration Tests**: End-to-end flows

---

## 🛠️ Customization

### Adding New Test Cases:
1. Open `functional_test_cases.csv`
2. Add new row with:
   - Test ID: TC091, TC092, etc.
   - Fill all columns
   - Set appropriate Priority
3. Save file
4. Re-run `convert_tests_to_excel.py` to update Excel

### Modifying Test Cases:
1. Edit CSV file directly
2. Update Test Steps, Expected Results, etc.
3. Re-run conversion script

### Filtering Test Cases:
- **By Module**: Filter Module column
- **By Priority**: Filter Priority column
- **By Status**: Filter Status column
- **By Keyword**: Search Test Case Name column

---

## 📈 Reporting

### Test Summary Report Template:
```
Test Execution Summary
=====================
Date: [Date]
Executed By: [Name]
Environment: [Environment]

Total Test Cases: 90
- Executed: X
- Passed: Y
- Failed: Z
- Blocked: W
- Skipped: V

Pass Rate: (Y/X) × 100%

Critical Tests:
- Total: 15
- Passed: X
- Failed: Y

High Priority Tests:
- Total: 35
- Passed: X
- Failed: Y

Defects Found: [Count]
- Critical: [Count]
- High: [Count]
- Medium: [Count]
- Low: [Count]
```

---

## 💡 Tips for Test Execution

1. **Start with Critical Tests**: Execute critical priority tests first
2. **Follow Test Steps Exactly**: Don't skip steps
3. **Document Everything**: Record actual results, even if they match expected
4. **Take Screenshots**: For failed tests, capture screenshots
5. **Test in Clean Environment**: Use fresh test data when possible
6. **Verify Preconditions**: Ensure all preconditions are met before testing
7. **Test Both Positive and Negative**: Test valid and invalid scenarios
8. **Check Edge Cases**: Test boundary conditions (file size limits, etc.)

---

## 🔗 Integration with Test Management Tools

### Jira Integration:
- Import CSV to Jira Test Management
- Link test cases to user stories
- Track execution in Jira

### TestRail Integration:
- Import CSV to TestRail
- Organize by test suites
- Generate reports

### Excel/Google Sheets:
- Use directly for small teams
- Share via cloud for collaboration
- Use filters and pivot tables for analysis

---

## 📞 Support

For questions or issues with test scripts:
1. Review this README
2. Check test case descriptions in CSV
3. Verify test data is correct
4. Ensure preconditions are met

---

## ✅ Checklist Before Demo

- [ ] All Critical tests executed and passed
- [ ] All High priority tests executed and passed
- [ ] Test execution template filled
- [ ] Defects logged and tracked
- [ ] Test summary report generated
- [ ] Screenshots captured for key scenarios
- [ ] Test data prepared
- [ ] Test environment ready

---

**Happy Testing! 🚀**


