def generate_patient_briefing(patient_name, cob_result):
    return f"""
============================================================
                 PATIENT BRIEFING AUDITOR
============================================================
Hello {patient_name},

We have completed an automated multi-plan Coordination of Benefits (COB) 
assessment for your upcoming healthcare claims.

Here is the straightforward breakdown of your coverage:
* Total Expected Treatment Cost: ₹ {cob_result.total_cost:,.2f}
* Paid by your Primary Insurance: ₹ {cob_result.primary_covered:,.2f}
* Paid by your Secondary Insurance: ₹ {cob_result.secondary_covered:,.2f}

------------------------------------------------------------
👉 Your Final Out-of-Pocket Responsibility: ₹ {cob_result.patient_responsibility:,.2f}
============================================================
"""