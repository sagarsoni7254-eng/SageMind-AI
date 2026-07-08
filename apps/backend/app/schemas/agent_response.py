from typing import Any

from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    agent: str
    status: str
    confidence: float = Field(ge=0.0, le=1.0)
    execution_time_ms: int
    data: dict[str, Any]
    warnings: list[str] = []
    errors: list[str] = []