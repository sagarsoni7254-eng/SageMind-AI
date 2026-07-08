from app.orchestrator.research_orchestrator import research_orchestrator


class ResearchService:

    def analyze_stock(self, symbol: str):
        return research_orchestrator.run(symbol)


research_service = ResearchService()