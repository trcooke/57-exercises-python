import unittest

from exercises.Ex07_area_of_a_rectangular_room.rectangular_room import RectangularRoom


class TestRectangularRoom(unittest.TestCase):


    def test_given15FeetBy20Feet_thenArea300SquareFeet(self):
        rectangularRoom = RectangularRoom(15, 20)
        self.assertEqual(rectangularRoom.areaFeet(), 300)

    def test_given15FeetBy20Feet_thenArea27point871SquareMeters(self):
        rectangularRoom = RectangularRoom(15, 20)
        self.assertEqual(rectangularRoom.areaMeters(), 27.871)
