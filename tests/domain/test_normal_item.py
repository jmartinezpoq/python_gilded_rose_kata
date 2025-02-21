import unittest

from domain.items.normal import NormalItem


class NormalModelTest(unittest.TestCase):
    def test_normal_item_updates_quality(self) -> None:
        item = NormalItem("foo", 1, 1)

        item.update_quality()

        self.assertEqual(0, item.quality)

    def test_normal_item_updates_quality_twice_when_sell_in_zero(self) -> None:
        item = NormalItem("foo", -1, 2)

        item.update_quality()

        self.assertEqual(0, item.quality)

    def test_normal_item_updates_sell_in(self) -> None:
        item = NormalItem("foo", 1, 1)

        item.decrease_sell_in()

        self.assertEqual(0, item.sell_in)


if __name__ == "__main__":
    unittest.main()
