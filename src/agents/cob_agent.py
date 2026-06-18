from state import PatientAssessmentState, FinancialBreakdown

def determine_primary_plan(patient_name: str) -> dict:
    if patient_name.lower() == "aarav":
        return {"primary": "Plan B (Insurer2)", "secondary": "Plan A (Insurer1)"}
    elif patient_name.lower() == "priya":
        return {"primary": "Plan A (Insurer1)", "secondary": "Plan B (Insurer2)"}
    return {"primary": "Unknown", "secondary": "Unknown"}

def calculate_true_cob(total_cost: float, primary_plan: dict, secondary_plan: dict) -> FinancialBreakdown:
    p_deductible = primary_plan["deductible"]
    p_coinsurance = primary_plan["coinsurance"]
    
    p_allowed = max(0.0, total_cost - p_deductible)
    primary_payment = p_allowed * p_coinsurance
    patient_remaining = total_cost - primary_payment
    
    s_deductible = secondary_plan["deductible"]
    s_coinsurance = secondary_plan["coinsurance"]
    
    s_allowed = max(0.0, total_cost - s_deductible)
    s_normal_benefit = s_allowed * s_coinsurance
    
    secondary_payment = min(patient_remaining, s_normal_benefit)
    final_patient_responsibility = total_cost - (primary_payment + secondary_payment)
    
    return FinancialBreakdown(
        total_cost=total_cost,
        primary_covered=round(primary_payment, 2),
        secondary_covered=round(secondary_payment, 2),
        patient_responsibility=round(final_patient_responsibility, 2)
    )

def run_cob_agent(state: PatientAssessmentState) -> PatientAssessmentState:
    print("[PROCESSING] [COB Agent] Executing multi-plan liability calculations...")
    
    PLAN_A = {"name": "Plan A (Insurer1)", "deductible": 10000.0, "coinsurance": 0.80}
    PLAN_B = {"name": "Plan B (Insurer2)", "deductible": 5000.0, "coinsurance": 0.90}
    
    aarav_data = state.extracted_medical_data.get("aarav", {})
    if aarav_data:
        state.cob_calculations["aarav"] = calculate_true_cob(
            total_cost=aarav_data["total_cost"],
            primary_plan=PLAN_B,
            secondary_plan=PLAN_A
        )
        
    priya_data = state.extracted_medical_data.get("priya", {})
    if priya_data:
        state.cob_calculations["priya"] = calculate_true_cob(
            total_cost=priya_data["total_cost"],
            primary_plan=PLAN_A,
            secondary_plan=PLAN_B
        )
        
    state.next_action = "generate_outputs"
    print(f"[SUCCESS] [COB Agent] Insurance processing finished. Next action: {state.next_action}")
    return state