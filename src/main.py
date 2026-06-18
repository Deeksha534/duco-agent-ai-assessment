import os
import sys

# Initialize system path routing environments
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "agents"))

from state import PatientAssessmentState
from agents.intake_agent import run_multimodal_intake
from agents.cob_agent import run_cob_agent
from parsers.text_parser import read_text_file
from agents.cost_flow_agent import generate_cost_flow
from agents.briefing_agent import generate_patient_briefing
from agents.report_agent import generate_financial_report
from agents.letter_agent import generate_preauth_letter

def main():
    print("[INFO] [DuCO-Agent System] Initializing Multi-Agent Coordination Loop...")

    # Ensure mock data files exist to avoid crashing
    os.makedirs("data", exist_ok=True)
    query_path = "data/user_query.txt"
    if not os.path.exists(query_path):
        with open(query_path, "w", encoding="utf-8") as f:
            f.write("Hi DuCO-Agent, I need to get my knee operated on soon, and Priya has some physical therapy bills lying around. We have Insurer1 (Plan A) and Insurer2 (Plan B). Can you help us figure out which plan pays first for my surgery and her bills? How much will we actually have to pay out of our own pocket? Also, we need the pre-auth letters generated for both insurers so we don't end up with a claim rejection. Please help!")

    mock_assets = [
        "data/priya_pt_invoice.png",
        "data/aarav_mri_report.pdf",
        "data/surgeon_estimate.jpg"
    ]

    raw_query = read_text_file(query_path)
    state = PatientAssessmentState(user_query=raw_query, file_paths=mock_assets)

    # 1. Multi-Modal Intake Extraction Phase
    state = run_multimodal_intake(state, mock_assets)

    if not state.is_valid:
        print(f"[FATAL] Orchestrator halted execution: {state.validation_issues}")
        return

    # 2. Compliant Coordination of Benefits (COB) Calculation Phase
    state = run_cob_agent(state)

    # 3. Output Generation & Artifact Export Phase
    os.makedirs("outputs", exist_ok=True)
    
    aarav_calc = state.cob_calculations["aarav"]
    priya_calc = state.cob_calculations["priya"]
    
    aarav_data = state.extracted_medical_data["aarav"]
    priya_data = state.extracted_medical_data["priya"]

    # Export Visual Cost Outlay Flow
    with open("outputs/cost_flow_report.txt", "w", encoding="utf-8") as f:
        f.write(generate_cost_flow(aarav_calc))

    # Export Plain Narrative Consumer Briefing
    with open("outputs/patient_briefing.txt", "w", encoding="utf-8") as f:
        f.write(generate_patient_briefing("Aarav & Priya Sen", aarav_calc))

    # Export Executive Financial Summaries
    with open("outputs/financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(generate_financial_report("Aarav Sen", aarav_calc))

    with open("outputs/priya_financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(generate_financial_report("Priya Sen", priya_calc))

    # Export Pre-Authorization Letters for BOTH Insurers/Claims as requested
    aarav_letter = generate_preauth_letter(
        patient_name=aarav_data["patient_name"],
        diagnosis=aarav_data["condition"],
        procedures=aarav_data["procedures"],
        total_cost=aarav_calc.total_cost,
        primary_plan="Plan B (Insurer2)",
        secondary_plan="Plan A (Insurer1)"
    )
    with open("outputs/aarav_preauth_letter.txt", "w", encoding="utf-8") as f:
        f.write(aarav_letter)

    priya_letter = generate_preauth_letter(
        patient_name=priya_data["patient_name"],
        diagnosis=priya_data["condition"],
        procedures=priya_data["procedures"],
        total_cost=priya_calc.total_cost,
        primary_plan="Plan A (Insurer1)",
        secondary_plan="Plan B (Insurer2)"
    )
    with open("outputs/priya_preauth_letter.txt", "w", encoding="utf-8") as f:
        f.write(priya_letter)

    print("\n[SUCCESS] [DuCO-Agent System] Run Complete! All required assets stored successfully inside /outputs:")
    print(" -> outputs/cost_flow_report.txt")
    print(" -> outputs/patient_briefing.txt")
    print(" -> outputs/financial_summary.txt")
    print(" -> outputs/priya_financial_summary.txt")
    print(" -> outputs/aarav_preauth_letter.txt")
    print(" -> outputs/priya_preauth_letter.txt")

if __name__ == "__main__":
    main()