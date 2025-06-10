from pydantic import BaseModel
from typing import List, Any, Optional

class MCPResponse(BaseModel):
    result: Optional[Any] = None
    error: Optional[Any] = None