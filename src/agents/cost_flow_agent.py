def generate_cost_flow(cob_result):

    report = f"""
COST FLOW SUMMARY

Total Cost:
₹{cob_result["total_cost"]}

├── Primary Insurance
│   ₹{cob_result["primary_payment"]}

├── Secondary Insurance
│   ₹{cob_result["secondary_payment"]}

└── Patient Responsibility
    ₹{cob_result["patient_payment"]}
"""

    return report