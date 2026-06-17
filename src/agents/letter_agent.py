def generate_preauth_letter(patient_name: str, diagnosis: str, procedures: list, total_cost: float, primary_plan: str, secondary_plan: str) -> str:
    procedure_lines = ""
    for proc in procedures:
        procedure_lines += f"- CPT Code: {proc['cpt']} | Description: {proc['description']} | Cost: ₹ {proc['cost']:,.2f}\n"

    letter = f"""============================================================
              PRIOR AUTHORIZATION COMPLIANCE REQUEST
============================================================
Date: June 17, 2026
To: Medical Review Board & Prior Authorization Intake Dept.
Primary Coverage Carrier  : {primary_plan}
Secondary Coverage Carrier: {secondary_plan}

PATIENT CLINICAL PROFILE:
-------------------------
Patient Name : {patient_name}
Diagnosis    : {diagnosis}
Total Cost   : ₹ {total_cost:,.2f}

PROPOSED TREATMENT PLAN & CLINICAL CODES:
-----------------------------------------
{procedure_lines}
JUSTIFICATION & COMPLIANCE STATEMENT:
This request is submitted under dual Coordination of Benefits (COB) rules.
All clinical findings conform to policy validation checks. Please review
the attached structured intake data logs for expedited approval.

Authorized Signature: DuCO-Agent Processing Engine
============================================================
"""
    return letter