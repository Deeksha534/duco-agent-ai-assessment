def generate_cost_flow(cob_result):
    report = f"""
============================================================
                     VISUAL COST FLOW
============================================================
Total Gross Treatment Cost:
₹ {cob_result.total_cost:,.2f}
   │
   ├── [Primary Plan Allocation]
   │   └── Approved Payment: ₹ {cob_result.primary_covered:,.2f}
   │
   ├── [Secondary Plan Allocation]
   │   └── Approved Payment: ₹ {cob_result.secondary_covered:,.2f}
   │
   └── [Patient Final Out-of-Pocket Balance]
       └── Net Responsibility: ₹ {cob_result.patient_responsibility:,.2f}
============================================================
"""
    return report