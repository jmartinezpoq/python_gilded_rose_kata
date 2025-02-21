from typing import List

from domain.items.base import Item


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            item.decrease_sell_in()
            item.update_quality()
