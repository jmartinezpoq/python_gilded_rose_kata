from typing import List

from domain.item import Item

BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"

AGED_BRIE = "Aged Brie"

SULFURAS = "Sulfuras, Hand of Ragnaros"

MAX_QUALITY = 50


class GildedRose(object):

    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == SULFURAS:
                continue

            item.sell_in = self.__decrease_sell_in(item)

            if item.name == BACKSTAGE_PASS:
                item.quality = self.__increase_quality_for_backstage_pass(item)
                continue

            if item.name == AGED_BRIE:
                item.quality = self.__increase_quality_for_aged_brie(item)
                continue

            if item.quality > 0:
                item.quality = self.__reduce_quality_for_normal_item(item)

    def __decrease_sell_in(self, item: Item) -> int:
        return int(item.sell_in - 1)

    def __calculate_multiplier_for_normal_item(self, item: Item) -> int:
        multiplier = 1
        if item.sell_in < 0:
            multiplier = 2

        return multiplier

    def __calculate_multiplier_for_backstage_pass(self, item: Item) -> int:
        if item.sell_in < 0:
            return 0
        if item.sell_in < 5:
            return 3
        if item.sell_in < 10:
            return 2

        return 1

    def __increase_quality_for_aged_brie(self, item: Item) -> int:
        if item.quality < MAX_QUALITY:
            return int(item.quality + 1)

        return int(item.quality)

    def __increase_quality_for_backstage_pass(self, item: Item) -> int:
        if item.sell_in < 0:
            return 0

        multiplier = self.__calculate_multiplier_for_backstage_pass(item)
        if item.quality < MAX_QUALITY:
            return int(item.quality + 1 * multiplier)

        return int(item.quality)

    def __reduce_quality_for_normal_item(self, item: Item) -> int:
        multiplier = self.__calculate_multiplier_for_normal_item(item)

        if item.quality > 0:
            return int(item.quality - 1 * multiplier)

        return int(item.quality)
