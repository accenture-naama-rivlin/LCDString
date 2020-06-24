import lcd
import unittest

class TestLcdStringGenerator(unittest.TestCase):

    generator = lcd.LcdStringGenerator()

    def test_no_input_returns_empty_grid(self):
        self.assertEqual("...\n...\n...", self.generator.generate())

    def test_zero_returns_representation(self):
        self.assertEqual("._.\n|.|\n|_|", self.generator.generate(0))

    def test_one_returns_representation(self):
        self.assertEqual("...\n..|\n..|", self.generator.generate(1))

    def test_two_returns_representation(self):
        self.assertEqual("._.\n._|\n|_.", self.generator.generate(2))

    def test_three_returns_representation(self):
        self.assertEqual("._.\n._|\n._|", self.generator.generate(3))

    def test_four_returns_representation(self):
        self.assertEqual("...\n|_|\n..|", self.generator.generate(4))

    def test_five_returns_representation(self):
        self.assertEqual("._.\n|_.\n._|", self.generator.generate(5))

    def test_six_returns_representation(self):
        self.assertEqual("._.\n|_.\n|_|", self.generator.generate(6))

    def test_seven_returns_representation(self):
        self.assertEqual("._.\n..|\n..|", self.generator.generate(7))

    def test_eight_returns_representation(self):
        self.assertEqual("._.\n|_|\n|_|", self.generator.generate(8))

import unittest

if __name__ == "__main__":
    unittest.main()