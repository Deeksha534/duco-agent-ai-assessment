def generate_preauth_letter(
    patient_name,
    diagnosis,
    procedure_1,
    procedure_2,
    total_cost,
    primary_plan,
    secondary_plan
):

    letter = f"""
PRE-AUTHORIZATION REQUEST

Patient Name: {patient_name}

Diagnosis:
{diagnosis}

Requested Procedures:

1. CPT {procedure_1["cpt"]}
   {procedure_1["description"]}

2. CPT {procedure_2["cpt"]}
   {procedure_2["description"]}

Estimated Total Cost:
₹{total_cost}

Primary Insurance:
{primary_plan}

Secondary Insurance:
{secondary_plan}

This procedure has been recommended based on
clinical findings and is considered medically
necessary.

Kindly review this request and provide
pre-authorization approval.

Thank you.

Sincerely,
DuCO-Agent
"""

    return letter