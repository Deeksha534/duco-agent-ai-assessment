def decide_next_steps(info):

    actions = []

    if "aarav" in info:
        actions.append("mri_analysis")

    if (
        "aarav" in info
        and info["aarav"].get("requires_preauth")
    ):
        actions.append("generate_preauth_letter")

    if len(info) > 1:
        actions.append("calculate_cob")

    actions.append("generate_reports")

    return actions

def validate_case(info):

    validation_result = {
        "valid": True,
        "issues": []
    }

    if "aarav" not in info:
        validation_result["valid"] = False
        validation_result["issues"].append(
            "Missing Aarav case information"
        )

    if (
        "aarav" in info
        and not info["aarav"].get(
            "requires_preauth",
            False
        )
    ):
        validation_result["issues"].append(
            "Pre-authorization not detected"
        )

    return validation_result