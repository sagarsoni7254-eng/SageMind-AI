from app.agents.registry import registry


class ResearchOrchestrator:

    def run(self, symbol: str):

        results = []

        for agent in registry.get_all_agents():
            results.append(agent.run(symbol))

        return {
            "symbol": symbol.upper(),
            "status": "Research completed",
            "agents_executed": len(results),
            "results": results,
        }


research_orchestrator = ResearchOrchestrator()