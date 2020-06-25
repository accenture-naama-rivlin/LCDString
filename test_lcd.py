import lcd
import unittest

class TestLcdStringGenerator(unittest.TestCase):

    generator = lcd.LcdStringGenerator()

    def test_zero_returns_representation(self):
        self.assertEqual("._. \n|.| \n|_| \n", self.generator.generate(0))

    def test_one_returns_representation(self):
        self.assertEqual("... \n..| \n..| \n", self.generator.generate(1))

    def test_two_returns_representation(self):
        self.assertEqual("._. \n._| \n|_. \n", self.generator.generate(2))

    def test_three_returns_representation(self):
        self.assertEqual("._. \n._| \n._| \n", self.generator.generate(3))

    def test_four_returns_representation(self):
        self.assertEqual("... \n|_| \n..| \n", self.generator.generate(4))

    def test_five_returns_representation(self):
        self.assertEqual("._. \n|_. \n._| \n", self.generator.generate(5))

    def test_six_returns_representation(self):
        self.assertEqual("._. \n|_. \n|_| \n", self.generator.generate(6))

    def test_seven_returns_representation(self):
        self.assertEqual("._. \n..| \n..| \n", self.generator.generate(7))

    def test_eight_returns_representation(self):
        self.assertEqual("._. \n|_| \n|_| \n", self.generator.generate(8))

    def test_nine_returns_representation(self):
        self.assertEqual("._. \n|_| \n..| \n", self.generator.generate(9))

    def test_ten_returns_representation(self):
        self.assertEqual("... ._. \n..| |.| \n..| |_| \n", self.generator.generate(10))

import unittest

if __name__ == "__main__":
    unittest.main()