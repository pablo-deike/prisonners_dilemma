from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
