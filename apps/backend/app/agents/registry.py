from app.agents.market_agent import MarketAgent


class AgentRegistry:
    """
    Stores all available research agents.
    """

    def __init__(self):
        self._agents = [
            MarketAgent(),
        ]

    def get_all_agents(self):
        return self._agents


registry = AgentRegistry()