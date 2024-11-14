from abc import ABC, abstractmethod


class NoMemoryStrategy(ABC):

    @abstractmethod
    def play(self) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
