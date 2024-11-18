from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def get_final_score(self, points: int) -> None:
        pass

    @abstractmethod
    def get_average_scores(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
