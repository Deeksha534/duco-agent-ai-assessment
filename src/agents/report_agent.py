def generate_financial_report(
    patient_name,
    cob_result
):

    report = f"""
FINANCIAL SUMMARY REPORT

Patient: {patient_name}

Total Cost:
₹{cob_result["total_cost"]}

Primary Insurance Payment:
₹{cob_result["primary_payment"]}

Secondary Insurance Payment:
₹{cob_result["secondary_payment"]}

Patient Responsibility:
₹{cob_result["patient_payment"]}
"""

    return report