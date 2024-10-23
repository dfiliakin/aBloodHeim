from abc import abstractmethod


class Scene:
    NAME = "Undefined"

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError()
