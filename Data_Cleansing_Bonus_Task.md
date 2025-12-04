# Data Quality Analysis and Remediation Assignment
## Customer 360 Dataset - UK Market

---

## Assignment Overview

You have been provided with a customer 360 dataset containing information about UK customers. This dataset has been extracted from a legacy CRM system and contains various data quality issues that need to be identified, documented, and corrected.

Your task is to perform comprehensive data quality analysis, document all issues found, and deliver a clean, corrected dataset.

---

## Dataset Description

**File**: `customer_360_dataset.csv`

The dataset contains 100 customer records with the following attributes:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| customer_id | String | Unique customer identifier (format: UK-XXX) |
| first_name | String | Customer's first name |
| last_name | String | Customer's last name  |
| gender | String | Gender (M/F) |
| age | Integer | Customer's age in years |
| date_of_birth | Date | Date of birth (YYYY-MM-DD format) |
| address_line_1 | String | Primary address (street number and name) |
| address_line_2 | String | Secondary address (flat/apartment, optional) |
| city | String | UK city |
| postcode | String | UK postcode |
| email | String | Email address |
| mobile_number | String | UK mobile number (+44 format) |
| first_transaction_date | Date | Date of first transaction |
| last_transaction_date | Date | Date of most recent transaction |
| number_of_transactions | Integer | Total number of transactions |
| customer_lifetime_value | Float | Total revenue from customer (GBP) |
| attrition_probability | Float | Probability of customer churn (0-1) |
| number_of_products | Integer | Number of products purchased |
| customer_status | String | Current status (active/inactive/prospect/suspended) |

---

## Data Quality Score

The dataset has an **overall quality score of 72/100** (Moderate Quality), indicating significant data quality issues that require remediation.

---

## Known Issue Categories

Your analysis should identify and address the following types of data quality issues present in the dataset:

### 1. **Duplicate Records**
- Non-trivial duplicates with slight variations
- Require fuzzy matching techniques for identification
- Need deduplication strategy preserving maximum information

### 2. **Missing Values**
- NULL or empty values in various fields
- Some missing values can be imputed from duplicate records
- Others may require statistical imputation methods

### 3. **Typos and Incorrect Values**
- Invalid data formats
- Incorrect categorical values
- Negative values where only positive values are logical
- Date format inconsistencies

### 4. **Primary Key Gaps**
- Missing customer_id values
- Breaks referential integrity
- Requires unique ID assignment

### 5. **Inconsistent Values**
- Logical inconsistencies between related fields
- Values that violate business rules
- Temporal inconsistencies

### 6. **Syntax Errors**
- Incorrect format for structured fields (email, phone, postcode)
- Non-standard delimiters or patterns
- Invalid codes or prefixes

### 7. **Suspicious Patterns**
- Unusual clustering or gaps in temporal data
- Statistical anomalies suggesting batch processing issues
- Potential data entry artifacts

---

## Assignment Tasks

### Task 1: Data Quality Analysis (7.5 points)

1. **Load and Explore the Dataset**
   - Load the CSV file into Python/R
   - Perform initial exploratory data analysis
   - Generate summary statistics

2. **Identify All Data Quality Issues**
   - Systematically check each issue category
   - Document specific records affected
   - Count total occurrences of each issue type

3. **Document Your Findings**
   - Create a detailed report of all issues found
   - Include specific examples (record numbers, values)
   - Categorize issues by severity (High/Medium/Low)

### Task 2: Data Quality Remediation (10 points)

1. **Handle Duplicate Records**
   - Identify all duplicate pairs
   - Implement deduplication strategy
   - Merge records preserving complete information

2. **Impute Missing Values**
   - First: Impute from duplicate records where available
   - Second: Apply appropriate statistical methods for remaining values
   - Document imputation methodology

3. **Correct Data Errors**
   - Fix typos and incorrect values
   - Standardize date formats
   - Correct invalid categorical values
   - Address negative values

4. **Assign Missing Primary Keys**
   - Generate unique customer_id for records with NULL values
   - Maintain consistent format (UK-XXX)

5. **Resolve Inconsistencies**
   - Fix logical inconsistencies between fields
   - Correct temporal violations
   - Ensure business rule compliance

6. **Standardize Syntax**
   - Apply consistent UK formats to:
     - Mobile numbers: +44 7XXX XXX XXX
     - Postcodes: Proper UK format with space
     - Email addresses: Valid email format

7. **Address Suspicious Patterns**
   - Investigate date clustering
   - Document anomalies
   - Decide on appropriate action

### Task 3: Documentation (7.5 points)

Create comprehensive documentation including:

1. **Issue Report**: Detailed description of all issues found
   - Issue type
   - Number of affected records
   - Specific examples
   - Severity assessment

2. **Remediation Log**: Documentation of all corrections made
   - For each issue: what was wrong and how it was fixed
   - Imputation methods used
   - Business rules applied

3. **Data Quality Metrics**: Before and after comparison
   - Completeness (% of non-null values)
   - Accuracy (% of valid values)
   - Consistency (% of logically consistent records)
   - Uniqueness (% of non-duplicate records)

---

## Deliverables

You must submit the following files:

### 1. Original Dataset
- **File**: `customer_360_dataset.csv` (provided)
- Do not modify the original file

### 2. Documented Issues Report
- **File**: `data_quality_issues_report.pdf` or `data_quality_issues_report.docx`
- Comprehensive documentation of all issues found
- Include tables, charts, and specific examples
- Remediation log
- Data Quality metrics

### 3. Corrected Dataset
- **File**: `customer_360_dataset_cleaned.csv`
- The dataset after all remediation steps
- Must maintain same column structure as original
- Should have 96 records or fewer (after deduplication)

### 4. The Code You Used

---

## Evaluation Criteria

### Data Quality Analysis
- **Completeness**: Did you find all issue types?
- **Accuracy**: Are your findings correct?
- **Documentation**: Is your analysis well-documented?

### Data Remediation
- **Correctness**: Are the fixes appropriate and correct?
- **Completeness**: Were all issues addressed?
- **Methodology**: Did you use appropriate techniques?
- **Preservation**: Was valid data preserved during cleaning?

### Documentation
- **Clarity**: Are issues clearly explained?
- **Detail**: Sufficient detail and examples provided?
- **Structure**: Well-organized and professional?
- **Insights**: Do you provide meaningful analysis?

---

## UK Data Format Standards

When cleaning the data, ensure adherence to these UK-specific formats:

### **Mobile Phone Numbers**:
- Format: `+44 7XXX XXX XXX`
- Example: `+44 7777 123 456`
- Note: UK mobile numbers always start with 07 (7 after country code)

### **Postcodes**:
- Format: Outward code + space + Inward code
- Examples: `SW1A 1AA`, `M1 1AE`, `B1 1BB`
- Common error: Missing or extra spaces

### **Email Addresses**:
- Standard email format: `name@domain.extension`
- Common UK domains: .co.uk, .com, .org.uk

### **Date Format**:
- Standard: `YYYY-MM-DD`
- Example: `1985-03-15`

---

## Helpful Hints

### For Duplicate Detection:
- Consider using fuzzy matching on names and addresses
- Look for records with identical core attributes (name, DOB, email)
- Don't rely only on exact matching

### For Missing Value Imputation:
- Check if duplicate records have the missing value
- Use appropriate imputation methods (mean, median, mode) based on data type
- Document your imputation strategy

### For Inconsistency Detection:
- Calculate age from date_of_birth and compare with age field
- Verify first_transaction_date < last_transaction_date
- Check if CLV is reasonable given number_of_transactions

### For Pattern Detection:
- Create histograms of first_transaction_date
- Look for unusual spikes or clusters
- Use statistical methods to identify outliers

### For UK Postcode Validation:
- UK postcodes have specific format rules
- Always contain exactly one space
- First part (outward code) varies in length

---

## Resources

### Suggested Python Libraries:
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `fuzzywuzzy` - Fuzzy string matching
- `datetime` - Date operations
- `re` - Regular expressions for pattern matching

### Suggested R Libraries:
- `tidyverse` - Data manipulation
- `stringdist` - Fuzzy matching
- `lubridate` - Date operations
- `mice` - Missing data imputation

---

## Submission Instructions

1. Create a ZIP file containing all deliverables
2. Name the file: `LastName_FirstName_DataQuality_Assignment.zip`
3. Ensure all files are properly named as specified
4. Include a README.txt file with any special instructions

**Due Date**: 15th January 2026

---

## Academic Integrity

- This is an individual assignment
- You may discuss general approaches with classmates
- All code and documentation must be your own work
- Cite any external resources or code used

---

## Questions?

If you have questions about the assignment:
- Check the dataset documentation first
- Post questions in the course forum
- Email the instructor

Good luck! This assignment will help you develop essential data quality skills used in real-world data engineering and analytics roles.
