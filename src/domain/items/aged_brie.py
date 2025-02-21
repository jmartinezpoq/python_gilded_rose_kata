from core.constants import ONE
from domain.items.base import Item


class AgedBrieItem(Item):
    def update_quality(self) -> None:
        if self.quality < self.MAX_QUALITY:
            self.quality += ONE
