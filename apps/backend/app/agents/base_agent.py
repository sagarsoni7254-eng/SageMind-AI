from abc import ABC, abstractmethod
from typing import Dict


class BaseAgent(ABC):
    """
    Base class for all SageMind AI agents.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, symbol: str) -> Dict:
        """
        Execute the agent.
        """
        pass