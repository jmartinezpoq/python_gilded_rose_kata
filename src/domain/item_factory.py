from domain.items.aged_brie import AgedBrieItem
from domain.items.backstage_pass import BackstagePassItem
from domain.items.base import Item
from domain.items.conjured import ConjuredItem
from domain.items.legendary import LegendaryItem
from domain.items.normal import NormalItem

CONJURED_ITEM_NAME = "Conjured"

LEGENDARY_ITEM_NAME = "Sulfuras, Hand of Ragnaros"

BACKSTAGE_PASS_ITEM_NAME = "Backstage passes to a TAFKAL80ETC concert"

AGED_BRIE_ITEM_NAME = "Aged Brie"


class ItemFactory:
    @staticmethod
    def build(name: str, sell_in: int, quality: int) -> Item:
        if CONJURED_ITEM_NAME in name:
            return ConjuredItem(name, sell_in, quality)

        if name == AGED_BRIE_ITEM_NAME:
            return AgedBrieItem(name, sell_in, quality)

        if name == BACKSTAGE_PASS_ITEM_NAME:
            return BackstagePassItem(name, sell_in, quality)

        if name == LEGENDARY_ITEM_NAME:
            return LegendaryItem(name, sell_in, quality)

        return NormalItem(name, sell_in, quality)
