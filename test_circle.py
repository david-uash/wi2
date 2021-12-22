import circle
import math
import unittest


class TestCircleArea(unittest.TestCase):
  def test_area_01(self):
    self.assertAlmostEqual(circle.circleArea(1),math.pi)
    self.assertAlmostEqual(circle.circleArea(1/math.pi**0.5),1)

  def test_area_02(self):
    self.assertRaises(ValueError,circle.circleArea,-2)
