from unittest import TestCase
from .context import stuff


class Stuff(TestCase):
    def test_two_plus_two(self):
        self.assertEquals(8, stuff.two_plus_two(), "what was two plus two again?")

    def test_four_plus_four(self):
        self.assertEquals(8, stuff.four_plus_four(), "what was four plus four again?")
