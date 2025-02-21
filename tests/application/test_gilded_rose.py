# -*- coding: utf-8 -*-
import unittest

from application.gilded_rose import GildedRose
from domain.item_factory import ItemFactory


class GildedRoseTest(unittest.TestCase):
    def test_normal_items_updates_quality(self) -> None:
        items = [ItemFactory.build("foo", 1, 1), ItemFactory.build("bar", 0, 2)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual("bar", items[1].name)
        self.assertEqual(0, items[1].quality)

    def test_normal_items_decrease_sell_in(self) -> None:
        items = [ItemFactory.build("foo", 1, 1), ItemFactory.build("bar", 0, 2)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual("bar", items[1].name)
        self.assertEqual(-1, items[1].sell_in)


if __name__ == "__main__":
    unittest.main()
