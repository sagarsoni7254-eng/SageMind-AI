import time

from app.agents.base_agent import BaseAgent
from app.schemas.agent_response import AgentResponse


class MarketAgent(BaseAgent):

    def __init__(self):
        super().__init__("Market Agent")

    def run(self, symbol: str):

        start = time.perf_counter()

        response = AgentResponse(
            agent=self.name,
            status="success",
            confidence=1.0,
            execution_time_ms=0,
            data={
                "provider": "Yahoo Finance",
                "symbol": symbol.upper(),
                "message": "Market data placeholder",
            },
            warnings=[],
            errors=[],
        )

        end = time.perf_counter()

        response.execution_time_ms = int((end - start) * 1000)

        return response.model_dump()