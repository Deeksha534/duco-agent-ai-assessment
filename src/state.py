from pydantic import BaseModel, Field
from typing import Dict, Any, List

class FinancialBreakdown(BaseModel):
    total_cost: float = 0.0
    primary_covered: float = 0.0
    secondary_covered: float = 0.0
    patient_responsibility: float = 0.0

class PatientAssessmentState(BaseModel):
    # Core inputs passed into the system loop
    user_query: str = ""
    
    # State data generated and extracted by the specialized agents
    extracted_medical_data: Dict[str, Any] = Field(default_factory=dict)
    cob_calculations: Dict[str, FinancialBreakdown] = Field(default_factory=dict)
    
    # Routing and diagnostic tracking flags
    validation_issues: List[str] = Field(default_factory=list)
    is_valid: bool = True
    next_action: str = "intake"