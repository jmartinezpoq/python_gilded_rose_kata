from core.constants import TWO, ONE
from domain.items.base import Item


class NormalItem(Item):
    def update_quality(self) -> None:
        multiplier = self.__get_quality_multiplier()
        if self.quality > self.ZERO:
            self.quality -= ONE * multiplier

    def __get_quality_multiplier(self) -> int:
        multiplier = ONE
        if self.sell_in < self.ZERO:
            multiplier = TWO

        return int(multiplier)
