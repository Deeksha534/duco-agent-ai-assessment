import os
from src.state import PatientAssessmentState
from src.agents.intake_agent import run_multimodal_intake
from src.agents.cob_agent import run_cob_agent
from src.parsers.text_parser import read_text_file
from src.agents.cost_flow_agent import generate_cost_flow
from src.agents.briefing_agent import generate_patient_briefing
from src.agents.report_agent import generate_financial_report
from src.agents.letter_agent import generate_preauth_letter

def main():
    print("🚀 [DuCO-Agent System] Initializing Multi-Agent Coordination Loop...")

    # Define paths to mock files required by the assessment guidelines
    query_path = "data/user_query.txt"
    mock_assets = [
        "data/priya_pt_invoice.png",
        "data/aarav_mri_report.pdf",
        "data/surgeon_estimate.jpg"
    ]

    # Ensure files exist safely before processing
    if not os.path.exists(query_path):
        print(f"❌ Error: Required file {query_path} not found.")
        return

    # Initialize state with raw data input
    raw_query = read_text_file(query_path)
    state = PatientAssessmentState(user_query=raw_query, file_paths=mock_assets)

    # 1. Execute Multi-Modal Intake Agent
    state = run_multimodal_intake(state, mock_assets)

    # 2. Dynamic Execution & Safety Routing Check
    if not state.is_valid:
        print(f"🛑 Execution halted by Orchestrator. Validation Failures: {state.validation_issues}")
        return

    # 3. Execute Coordination of Benefits Math Engine
    state = run_cob_agent(state)

    # 4. Generate Aesthetics and Usability Deliverables
    os.makedirs("outputs", exist_ok=True)
    
    aarav_calc = state.cob_calculations["aarav"]
    priya_calc = state.cob_calculations["priya"]

    # Generate Visual Cost Flow Report
    cost_flow_content = generate_cost_flow(aarav_calc)
    with open("outputs/cost_flow_report.txt", "w", encoding="utf-8") as f:
        f.write(cost_flow_content)

    # Generate Patient Narrative Audio Briefing
    patient_briefing_content = generate_patient_briefing("Aarav Sen", aarav_calc)
    with open("outputs/patient_briefing.txt", "w", encoding="utf-8") as f:
        f.write(patient_briefing_content)

    # Generate Structured Corporate Financial Summaries
    aarav_report = generate_financial_report("Aarav Sen", aarav_calc)
    with open("outputs/financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(aarav_report)

    priya_report = generate_financial_report("Priya Sen", priya_calc)
    with open("outputs/priya_financial_summary.txt", "w", encoding="utf-8") as f:
        f.write(priya_report)

    # Generate Clinical Pre-Authorization Approval Request Letter
    # Extracted metadata maps directly to surgical procedure layouts
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

    print("\n🎉 [DuCO-Agent System] Run Complete! All assets stored successfully inside /outputs:")
    print(" -> outputs/cost_flow_report.txt")
    print(" -> outputs/patient_briefing.txt")
    print(" -> outputs/financial_summary.txt")
    print(" -> outputs/priya_financial_summary.txt")
    print(" -> outputs/aarav_preauth_letter.txt")

if __name__ == "__main__":
    main()