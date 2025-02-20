from typing import List

from domain.item import Item

BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"

AGED_BRIE = "Aged Brie"

SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == SULFURAS:
                continue

            item.sell_in = self.__decrease_sell_in(item)

            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS:
                if item.quality > 0:
                    item.quality = self.__reduce_quality(item)
            else:
                if item.quality < 50:
                    item.quality = self.__increase_quality(item)
                    if item.name == BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = self.__increase_quality(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = self.__increase_quality(item)

            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASS:
                        if item.quality > 0:
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
