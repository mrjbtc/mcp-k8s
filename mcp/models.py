from pydantic import BaseModel
from typing import List, Any, Optional

class MCPResponse(BaseModel):
    result: Optional[List[Any]] = None
    error: Optional[Any] = None