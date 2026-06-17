import os
import sys

# Dynamic path initialization to fix Python's import engine registry
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

    query_path = "data/user_query.txt"
    mock_assets = [
        "data/priya_pt_invoice.png",
        "data/aarav_mri_report.pdf",
        "data/surgeon_estimate.jpg"
    ]

    if not os.path.exists(query_path):
        print(f"[ERROR] Required input file {query_path} was not located.")
        return

    raw_query = read_text_file(query_path)
    state = PatientAssessmentState(user_query=raw_query, file_paths=mock_assets)

    # 1. Run Intake Extraction
    state = run_multimodal_intake(state, mock_assets)

    # 2. Safety Flow Checks
    if not state.is_valid:
        print(f"[FATAL] Execution halted by Orchestrator. Validation Failures: {state.validation_issues}")
        return

    # 3. Calculate COB Metrics
    state = run_cob_agent(state)

    # 4. Generate Output Deliverables
    os.makedirs("outputs", exist_ok=True)
    
    aarav_calc = state.cob_calculations["aarav"]
    priya_calc = state.cob_calculations["priya"]

    with open("outputs/cost_flow_report.txt", "w", encoding="utf-8") as f:
        f.write(generate_cost_flow(aarav_calc))

    with open("outputs/patient_briefing.txt", "w", encoding="utf-8") as f:
        f.write(generate_patient_briefing("Aarav Sen", aarav_calc))

    with open("outputs/financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(generate_financial_report("Aarav Sen", aarav_calc))

    with open("outputs/priya_financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(generate_financial_report("Priya Sen", priya_calc))

    mock_cpt_1 = {"cpt": "29888", "description": "Arthroscopically aided ACL reconstruction"}
    mock_cpt_2 = {"cpt": "29881", "description": "Arthroscopy knee with meniscectomy"}
    
    preauth_letter = generate_preauth_letter(
        patient_name="Aarav Sen",
        diagnosis="Complete ACL Tear & Medial Meniscus Tear",
        procedure_1=mock_cpt_1,
        procedure_2=mock_cpt_2,
        total_cost=aarav_calc.total_cost,
        primary_plan="Plan B (Insurer2)",
        secondary_plan="Plan A (Insurer1)"
    )
    with open("outputs/aarav_preauth_letter.txt", "w", encoding="utf-8") as f:
        f.write(preauth_letter)

    print("\n[SUCCESS] [DuCO-Agent System] Run Complete! Artifacts securely stored inside /outputs.")

if __name__ == "__main__":
    main()