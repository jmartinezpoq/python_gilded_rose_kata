from abc import abstractmethod, ABC

from core.constants import ONE


class Item(ABC):
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    ZERO = 0
    MAX_QUALITY = 50

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @abstractmethod
    def update_quality(self) -> None:
        pass

    def decrease_sell_in(self) -> None:
        self.sell_in -= ONE
