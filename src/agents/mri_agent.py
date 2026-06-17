def analyze_mri_report(report_text):

    findings = {
        "acl_tear": False,
        "meniscus_tear": False
    }

    report_text = report_text.lower()

    if "acl" in report_text:
        findings["acl_tear"] = True

    if "meniscus" in report_text:
        findings["meniscus_tear"] = True

    return findings

def generate_diagnosis(findings):

    diagnosis_parts = []

    if findings["acl_tear"]:
        diagnosis_parts.append("Complete ACL Tear")

    if findings["meniscus_tear"]:
        diagnosis_parts.append("Medial Meniscus Tear")

    return " with ".join(diagnosis_parts)