def determine_primary_plan(patient_name):
    """
    Mock Coordination of Benefits logic
    """

    if patient_name.lower() == "aarav":
        return {
            "primary": "Plan B (Insurer2)",
            "secondary": "Plan A (Insurer1)"
        }

    elif patient_name.lower() == "priya":
        return {
            "primary": "Plan A (Insurer1)",
            "secondary": "Plan B (Insurer2)"
        }

    return {
        "primary": "Unknown",
        "secondary": "Unknown"
    }


def calculate_cob_claim(total_cost, primary_plan, secondary_plan):

    primary_deductible = primary_plan["deductible"]
    primary_coverage = primary_plan["coinsurance"]

    amount_after_primary_deductible = total_cost - primary_deductible

    primary_payment = amount_after_primary_deductible * primary_coverage

    remaining_balance = total_cost - primary_payment

    secondary_deductible = secondary_plan["deductible"]
    secondary_coverage = secondary_plan["coinsurance"]

    amount_after_secondary_deductible = max(
        0,
        remaining_balance - secondary_deductible
    )

    secondary_payment = (
        amount_after_secondary_deductible * secondary_coverage
    )

    patient_payment = (
        total_cost
        - primary_payment
        - secondary_payment
    )

    return {
        "total_cost": total_cost,
        "primary_payment": primary_payment,
        "secondary_payment": secondary_payment,
        "patient_payment": patient_payment
    }