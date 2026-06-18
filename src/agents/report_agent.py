def generate_financial_report(patient_name, cob_result):
    return f"""
============================================================
                FINANCIAL SUMMARY COMPLIANCE REPORT
============================================================
Patient Insured Name : {patient_name}
Gross Claim Liability: ₹ {cob_result.total_cost:,.2f}
------------------------------------------------------------
Primary Carrier Payment Allocation  : ₹ {cob_result.primary_covered:,.2f}
Secondary Carrier Payment Allocation: ₹ {cob_result.secondary_covered:,.2f}
------------------------------------------------------------
Total Assessed Out-of-Pocket Cost   : ₹ {cob_result.patient_responsibility:,.2f}
============================================================
"""