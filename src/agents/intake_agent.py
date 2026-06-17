from typing import List
from src.state import PatientAssessmentState

def run_multimodal_intake(state: PatientAssessmentState, mock_files: List[str]) -> PatientAssessmentState:
    print("✨ [Intake Agent] Actively ingest and process multi-modal mock inputs...")
    
    # Simulate processing text inputs and multi-modal binary content structurally
    query = state.user_query.lower()
    
    # 1. Parse 'priya_pt_invoice.png' (Simulated Multi-Modal Extraction)
    # The agent reads a scanned, crumpled invoice, reads handwritten notes, 
    # and maps "Physical Therapy Evaluation and Therapeutic Exercise" to CPT 97161 and 97110
    priya_extracted = {
        "patient_name": "Priya",
        "condition": "Chronic back pain",
        "total_cost": 30000.0,
        "procedures": [
            {"cpt": "97161", "description": "Physical Therapy Evaluation", "cost": 10000.0},
            {"cpt": "97110", "description": "Therapeutic Exercise", "cost": 20000.0}
        ],
        "requires_preauth": False
    }
    
    # 2. Parse 'aarav_mri_report.pdf' & 'surgeon_estimate.jpg'
    # Extracts text confirming ACL/meniscus tear and grabs the surgeon's breakdown
    aarav_extracted = {
        "patient_name": "Aarav",
        "condition": "Complete tear of ACL and medial meniscus tear",
        "total_cost": 450000.0,
        "procedures": [
            {"cpt": "29888", "description": "Arthroscopically aided ACL reconstruction", "cost": 350000.0},
            {"cpt": "29881", "description": "Arthroscopy, knee, surgical; with meniscectomy", "cost": 10000.0}
        ],
        "requires_preauth": True
    }
    
    # Consolidate inside our structured medical data schema
    state.extracted_medical_data = {
        "priya": priya_extracted,
        "aarav": aarav_extracted
    }
    
    # 3. Validation Loop & Reflection Strategy
    # Dynamically verify if information is missing or if everything is clean
    issues = []
    if "knee" not in query and "surgery" not in query:
        issues.append("Warning: Voice transcript did not mention knee surgery explicitly.")
    if not mock_files:
        issues.append("Error: No source image or PDF files were supplied to the ingestion layer.")
        state.is_valid = False
        
    state.validation_issues = issues
    
    # Determine the next agent step dynamically
    if state.is_valid:
        state.next_action = "calculate_cob"
    else:
        state.next_action = "error_handling"
        
    print(f"✅ [Intake Agent] Extraction and mapping complete. Next step: {state.next_action}")
    return state