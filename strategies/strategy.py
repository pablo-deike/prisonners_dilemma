from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def play(self, last_plays: list) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
