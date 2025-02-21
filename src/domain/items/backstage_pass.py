from core.constants import ONE, TWO, THREE
from domain.items.base import Item


class BackstagePassItem(Item):
    FIRST_THRESHOLD = 10
    SECOND_THRESHOLD = 5

    def update_quality(self) -> None:
        if self.sell_in < self.ZERO:
            self.quality = self.ZERO
            return

        multiplier = self.__get_quality_multiplier()
        if self.quality < self.MAX_QUALITY:
            self.quality += ONE * multiplier

    def __get_quality_multiplier(self) -> int:
        if self.sell_in < self.SECOND_THRESHOLD:
            return int(THREE)
        if self.sell_in < self.FIRST_THRESHOLD:
            return int(TWO)
        return int(ONE)
