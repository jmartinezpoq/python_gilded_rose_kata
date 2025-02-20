from typing import List

from domain.item import Item


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = self.__reduce_quality(item)
            else:
                if item.quality < 50:
                    item.quality = self.__increase_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = self.__increase_quality(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = self.__increase_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = self.__decrease_sell_in(item)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = self.__reduce_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = self.__increase_quality(item)

    def __decrease_sell_in(self, item: Item) -> int:
        return int(item.sell_in - 1)

    def __increase_quality(self, item: Item) -> int:
        return int(item.quality + 1)

    def __reduce_quality(self, item: Item) -> int:
        return int(item.quality - 1)
