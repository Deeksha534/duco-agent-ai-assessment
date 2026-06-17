def generate_patient_briefing(
    patient_name,
    cob_result
):

    return f"""
PATIENT BRIEFING

Hello {patient_name},

Your treatment request has been reviewed.

The total estimated treatment cost is
₹{cob_result["total_cost"]}.

Your primary insurance is expected to pay
₹{cob_result["primary_payment"]}.

Your secondary insurance is expected to pay
₹{cob_result["secondary_payment"]}.

Your estimated out-of-pocket payment is
₹{cob_result["patient_payment"]}.

A pre-authorization request has been prepared.

If approved, you may proceed with the treatment
as advised by your healthcare provider.

Thank you.
"""