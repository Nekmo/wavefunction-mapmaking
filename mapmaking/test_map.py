import unittest

from mapmaking.box import Box
from mapmaking.map import Map
from mapmaking.tiles import Tile


class MyTestCase(unittest.TestCase):
    def test_get_boxes_around(self):
        map = Map(3, 3)
        map[0][0] = Box(map, 0, 0)
        map[0][1] = Box(map, 0, 1)
        map[1][1] = Box(map, 1, 1)

        self.assertEqual(len(map.get_boxes_around(0, 0)), 2)
        self.assertEqual(len(map.get_boxes_around(0, 1)), 3)
        self.assertEqual(len(map.get_boxes_around(1, 1)), 4)

    def test_get_filled_boxes_around(self):
        map = Map(3, 3)
        map[1][1] = Box(map, 1, 1)
        map[1][1].possible_tiles = [Tile(None, ["a", "a", "a", "a"])]

        map[0][0] = Box(map, 0, 0)
        map[0][1] = Box(map, 0, 1)

        self.assertEqual(len(map.get_filled_boxes_around(0, 0)), 0)
        self.assertEqual(len(map.get_filled_boxes_around(0, 1)), 1)
        self.assertEqual(len(map.get_filled_boxes_around(1, 1)), 0)

    def test_get_relative_postition_of_given_box(self):
        map = Map(3, 3)

        self.assertEqual(
            map.get_relative_position_of_given_box(Box(map, 0, 1), Box(map, 0, 0)),
            "down"
        )
        self.assertEqual(
            map.get_relative_position_of_given_box(Box(map, 1, 1), Box(map, 1, 2)),
            "up"
        )
        self.assertEqual(
            map.get_relative_position_of_given_box(Box(map, 1, 1), Box(map, 2, 1)),
            "right"
        )
        self.assertEqual(
            map.get_relative_position_of_given_box(Box(map, 1, 1), Box(map, 0, 1)),
            "left"
        )

    def test_set_tile(self):
        map = Map(3, 3)
        map.set_tile(0, 0)

        self.assertEqual(len(map[0][0].possible_tiles), 1)

    def test_update_possible_tiles(self):
        map = Map(1, 2)
        map[0][0].possible_tiles = [Tile(None, ["a", "a", "a", "a"])]
        map.update_possible_tiles()

        self.assertEqual(len(map[0][1].possible_tiles), 20)
        for tile in map[0][1].possible_tiles:
            self.assertEqual(tile.frontier_list[2], "a")

    def test_get_smallest_entropy_box_unset(self):
        map = Map(3, 3)
        min_entropy_box = map.get_smallest_entropy_box()

        self.assertEqual(min_entropy_box.entropy, 50)

    def test_get_smallest_entropy_box(self):
        map = Map(3, 3)
        tile = Tile(None, ["a", "ta", "a", "a"])
        map[1][1].possible_tiles = [tile, tile, tile, tile]
        min_entropy_box = map.get_smallest_entropy_box()

        self.assertEqual(min_entropy_box.entropy, 4)



if __name__ == '__main__':
    unittest.main()
