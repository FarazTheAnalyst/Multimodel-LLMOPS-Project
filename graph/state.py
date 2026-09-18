import operator
from typing import Annotated, Any, DIct, List, Optional, TypedDict

# define the schema for a single compliance result
class ComplianceResult(TypedDict):
    category: str
    description: str # specific detail of violation
    severity: str   # CRITICAL | WARNING
    timestamp: Optional[str] # timestamp of the violation, if available

# define the global graph state
# this defines the state that gets passed between nodes in the agentic workflow
class VidoeAuditState(TypedDict):
    """
        defines the data schema for langgraph execution content
        Main container : holds all the infromation about the audit
        right from the initial URL ot the final report
    """  
    # input parameters
    video_url: str
    video: str

# ingestion and extraction data
local_file_path: Optional[str]
video_metadata: Optional[Dict[str, Any]] #{"duration": 15, "resolution": "1080p"}
transcript: Optional[str] # Fully extracted speech-to-text
ocr_text: List[str]

# analysis output
# stores the list of all the violaitons found by AI
compliance_results : Annotated[List[ComplianceResult], operator.add]

# analysis output
compliance_results : Annotated[list[ComplianceResult], operator.add]

# final deliverables
final_status : str # PASS | FAIL
final_report : str # markdown format

# system observability
# errors : API timeout, system level errors
# list of sysetem level crashes
error : Annotated[List[str], operator.add]
