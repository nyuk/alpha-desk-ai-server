from abc import ABC, abstractmethod


class SummarizationPort(ABC):
    @abstractmethod
    def summarize(self, content: str) -> str:
        pass
