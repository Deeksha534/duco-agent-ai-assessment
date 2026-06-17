from agents.intake_agent import intake
from agents.cob_agent import (
    determine_primary_plan,
    calculate_cob_claim
)
from agents.finance_agent import calculate_claim
from parsers.text_parser import read_text_file
from models.insurance_plans import PLAN_A, PLAN_B
from agents.letter_agent import generate_preauth_letter
from models.procedure_codes import (
    ACL_RECONSTRUCTION,
    MENISCECTOMY
)
from agents.mri_agent import (
    analyze_mri_report,
    generate_diagnosis
)
from agents.report_agent import generate_financial_report
# Read user query
user_query = read_text_file("data/user_query.txt")

# Extract information
info = intake(user_query)

print("Extracted Information:")
print(info)

# Aarav's insurance coordination
aarav_plan = determine_primary_plan("aarav")

print("\nAarav Insurance Coordination:")
print(aarav_plan)

# Priya's insurance coordination
priya_plan = determine_primary_plan("priya")

print("\nPriya Insurance Coordination:")
print(priya_plan)

# Single-plan calculations
print("\nAarav Claim Calculation:")
aarav_claim = calculate_claim(450000, PLAN_B)
print(aarav_claim)

print("\nPriya Claim Calculation:")
priya_claim = calculate_claim(30000, PLAN_A)
print(priya_claim)

# COB calculations
print("\nCOB Calculation For Aarav:")
aarav_cob = calculate_cob_claim(
    450000,
    PLAN_B,
    PLAN_A
)
print(aarav_cob)

print("\nFINANCIAL REPORT\n")

financial_report = generate_financial_report(
    "Aarav Sen",
    aarav_cob
)

print(financial_report)
print("\nPRIYA FINANCIAL REPORT\n")


print("\nCOB Calculation For Priya:")
priya_cob = calculate_cob_claim(
    30000,
    PLAN_A,
    PLAN_B
)
print(priya_cob)

priya_financial_report = generate_financial_report(
    "Priya",
    priya_cob
)
print(priya_financial_report)


print("\nMRI Analysis:")

mri_report = read_text_file("data/mri_report.txt")

mri_findings = analyze_mri_report(mri_report)

print(mri_findings)
diagnosis = generate_diagnosis(mri_findings)

print("\nGenerated Diagnosis:")
print(diagnosis)

print("\nPRE-AUTHORIZATION LETTER\n")

aarav_letter = generate_preauth_letter(
    "Aarav Sen",
     diagnosis,
    ACL_RECONSTRUCTION,
    MENISCECTOMY,
    450000,
    "Plan B (Insurer2)",
    "Plan A (Insurer1)"
)

print(aarav_letter)

with open(
    "outputs/aarav_preauth_letter.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(aarav_letter)

print(
    "\nLetter saved to outputs/aarav_preauth_letter.txt"
)

with open(
    "outputs/financial_summary.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(financial_report)

print(
    "Financial report saved to outputs/financial_summary.txt"
)
with open(
    "outputs/priya_financial_summary.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(priya_financial_report)

print(
    "Priya report saved to outputs/priya_financial_summary.txt"
)