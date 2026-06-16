def calculate_claim(total_cost, plan):
    """
    Insurance calculation with deductible and coinsurance
    """

    deductible = plan["deductible"]
    coinsurance = plan["coinsurance"]

    amount_after_deductible = total_cost - deductible

    insurance_payment = amount_after_deductible * coinsurance

    patient_payment = total_cost - insurance_payment

    return {
        "plan": plan["name"],
        "total_cost": total_cost,
        "deductible": deductible,
        "insurance_payment": insurance_payment,
        "patient_payment": patient_payment
    }