def intake(user_query):
    query = user_query.lower()

    extracted_info = {
        "aarav": {
            "knee_surgery": False,
            "requires_preauth": False
        },
        "priya": {
            "physical_therapy": False
        }
    }

    if "knee" in query:
        extracted_info["aarav"]["knee_surgery"] = True

    if "physical therapy" in query:
        extracted_info["priya"]["physical_therapy"] = True

    if "pre-auth" in query or "preauth" in query:
        extracted_info["aarav"]["requires_preauth"] = True

    return extracted_info