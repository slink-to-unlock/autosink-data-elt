from abc import ABC, abstractmethod


class BasePipe(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def __call__(self):
        raise NotImplementedError
