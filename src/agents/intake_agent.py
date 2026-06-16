def intake(user_query):
    extracted_info = {
        "knee_surgery": "knee" in user_query.lower(),
        "physical_therapy": "physical therapy" in user_query.lower()
    }

    return extracted_info