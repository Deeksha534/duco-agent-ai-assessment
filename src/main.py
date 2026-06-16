from agents.intake_agent import intake
from agents.cob_agent import determine_primary_plan
from parsers.text_parser import read_text_file
from agents.finance_agent import calculate_claim
from models.insurance_plans import PLAN_A, PLAN_B

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

print("\nAarav Claim Calculation:")
aarav_claim = calculate_claim(450000, PLAN_B)
print(aarav_claim)

print("\nPriya Claim Calculation:")
priya_claim = calculate_claim(30000, PLAN_A)
print(priya_claim)