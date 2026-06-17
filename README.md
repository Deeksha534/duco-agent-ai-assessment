# DuCO-Agent AI Assessment

The final implementation for this assessment is available on the feature/agent-state branch, which is also configured as the repository's default branch.

Earlier branches (e.g., feature/pdf-parser) are retained to demonstrate feature-based development workflow and commit history.

## Overview

DuCO-Agent is an Agentic Multi-Modal AI System designed to automate insurance coordination, medical document analysis, Coordination of Benefits (COB) calculations, financial responsibility estimation, and pre-authorization letter generation.

The system processes multi-modal healthcare inputs including PDF reports, scanned images, and user queries. It utilizes a state-driven multi-agent workflow to extract clinical information, validate inputs, determine insurance coordination rules, calculate claim liabilities, and generate patient-facing outputs.

---

## Features

### Multi-Modal Intake Agent

* Processes text, image, and PDF inputs
* Extracts contextual information from:

  * MRI reports
  * Physical therapy invoices
  * Surgeon estimation sheets
* Maintains centralized agent state
* Performs validation and routing

### MRI Analysis Agent

* Analyzes MRI report findings
* Detects ACL tears
* Detects meniscus tears
* Generates diagnosis summaries

### COB Agent

* Determines primary and secondary insurance plans
* Applies Coordination of Benefits (COB) logic
* Calculates insurance liabilities

### Finance Agent

* Calculates insurance payments
* Applies deductibles and coinsurance
* Computes patient responsibility

### Letter Agent

* Generates professional pre-authorization letters
* Includes CPT procedure codes
* Includes diagnosis information
* Generates insurer-ready documentation

### Report Agent

* Generates financial summary reports
* Generates patient-friendly cost breakdowns
* Produces cost flow visualizations

---

## Multi-Modal Inputs

The system processes the following inputs:

### Text Input

* user_query.txt

### PDF Input

* aarav_mri_report.pdf

### Image Inputs

* priya_pt_invoice.png
* surgeon_estimate.jpg

---

## Project Structure

duco-agent-ai-assessment

├── data/

│ ├── user_query.txt

│ ├── aarav_mri_report.pdf

│ ├── priya_pt_invoice.png

│ └── surgeon_estimate.jpg

│

├── outputs/

│ ├── financial_summary.txt

│ ├── priya_financial_summary.txt

│ ├── aarav_preauth_letter.txt

│ ├── priya_preauth_letter.txt

│ ├── patient_briefing.txt

│ └── cost_flow_report.txt

│

├── src/

│

│ ├── agents/

│ │ ├── intake_agent.py

│ │ ├── cob_agent.py

│ │ ├── finance_agent.py

│ │ ├── letter_agent.py

│ │ ├── mri_agent.py

│ │ └── report_agent.py

│ │

│ ├── parsers/

│ │ ├── text_parser.py

│ │ ├── pdf_parser.py

│ │ └── image_parser.py

│ │

│ ├── models/

│ │ ├── insurance_plans.py

│ │ └── procedure_codes.py

│ │

│ ├── state.py

│ └── main.py

│

├── requirements.txt

└── README.md

---

## Agentic Workflow

User Query

↓

Multi-Modal Intake Agent

↓

Validation Layer

↓

MRI Analysis Agent

↓

COB Agent

↓

Finance Agent

↓

Report Agent

↓

Letter Agent

↓

Output Generation

---

## Agent State Management

The system maintains a centralized state object that stores:

* Extracted medical information
* Financial calculations
* Validation results
* Agent routing decisions
* Generated artifacts

This enables dynamic workflow transitions between agents and supports validation-driven execution.

---

## Generated Outputs

The system generates:

### Financial Reports

* financial_summary.txt
* priya_financial_summary.txt

### Pre-Authorization Letters

* aarav_preauth_letter.txt
* priya_preauth_letter.txt

### Patient Communication

* patient_briefing.txt

### Cost Visualization

* cost_flow_report.txt

All generated files are stored inside the outputs/ directory.

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Run Application

python -m src.main

---

## Technologies Used

* Python
* Pydantic
* PyMuPDF
* Pillow
* pytesseract
* Git
* GitHub

---

## Future Improvements

* Real insurer API integration
* LLM-powered clinical reasoning
* Automated CPT inference from OCR text
* Advanced claim optimization strategies
* Interactive dashboard
* Voice-based patient briefing generation


Submission review branch for PR workflow demonstration.