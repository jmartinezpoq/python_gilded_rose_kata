from core.constants import TWO
from domain.items.base import Item


class ConjuredItem(Item):
    def update_quality(self) -> None:
        if self.quality > self.ZERO:
            self.quality -= TWO
