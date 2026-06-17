# DuCO-Agent AI Assessment

## Overview

DuCO-Agent is a multi-agent insurance coordination system designed to automate medical claim processing, Coordination of Benefits (COB), financial responsibility estimation, MRI report analysis, and pre-authorization letter generation.

The system processes patient requests, analyzes medical information, determines insurance coverage order, calculates claim payments, and generates supporting documentation.

---

## Features

### Intake Agent

* Parses user requests
* Identifies medical procedures
* Detects pre-authorization requirements

### MRI Analysis Agent

* Analyzes MRI report text
* Detects ACL tears
* Detects meniscus tears
* Generates diagnosis summaries

### COB Agent

* Determines primary and secondary insurance plans
* Calculates Coordination of Benefits (COB)

### Finance Agent

* Calculates insurance payments
* Applies deductibles and coverage percentages
* Computes patient responsibility

### Letter Agent

* Generates pre-authorization request letters
* Includes CPT procedure codes
* Includes diagnosis information

### Report Agent

* Generates financial summary reports
* Summarizes insurance payments and patient costs

---

## Project Structure

```text
duco-agent-ai-assessment
│
├── data/
│   ├── user_query.txt
│   └── mri_report.txt
│
├── outputs/
│   ├── aarav_preauth_letter.txt
│   └── financial_summary.txt
│
├── src/
│   │
│   ├── agents/
│   │   ├── intake_agent.py
│   │   ├── cob_agent.py
│   │   ├── finance_agent.py
│   │   ├── letter_agent.py
│   │   ├── mri_agent.py
│   │   └── report_agent.py
│   │
│   ├── models/
│   │   ├── insurance_plans.py
│   │   └── procedure_codes.py
│   │
│   ├── parsers/
│   │   ├── text_parser.py
│   │   ├── pdf_parser.py
│   │   └── image_parser.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Architecture

```text
User Query
     |
     v
Text / PDF / Image Parsers
     |
     v
Intake Agent
     |
     v
MRI Agent
     |
     v
COB Agent
     |
     v
Finance Agent
     |
     v
Report Agent + Letter Agent
     |
     v
Output Files
```

---

## Workflow

```text
User Query
      ↓
Text / PDF / Image Parsing
      ↓
Intake Agent
      ↓
MRI Analysis
      ↓
Diagnosis Generation
      ↓
Insurance Coordination
      ↓
COB Calculation
      ↓
Financial Report Generation
      ↓
Pre-Authorization Letter Generation
      ↓
Output Files
```


## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/main.py
```

---

## Generated Outputs

The application generates:

* Pre-Authorization Letter
* Financial Summary Report

Files are saved in:

```text
outputs/
```

---

## Technologies Used

* Python
* PyMuPDF
* Pillow
* pytesseract
* Git
* GitHub

---

## Future Improvements

* Real MRI PDF processing
* OCR-based invoice extraction
* Automated CPT code extraction
* Interactive dashboard
* Insurance API integration
* Advanced medical reasoning

```
```
