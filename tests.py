import unittest
from random import random, randint
from math import pow, pi

from figures import get_circle_area, get_triangle_area


class CircleAreaTestCase(unittest.TestCase):
    def test_negative_radius(self):
        for _ in range(1000):
            area = get_circle_area(-random() * randint(1, 1000))
            self.assertEqual(area, -1)
    
    def test_positive_radius(self):
        for _ in range(1000):
            random_radius = random() * randint(0, 1000)
            area = get_circle_area(random_radius)
            self.assertAlmostEqual(area, pow(random_radius, 2) * pi)


class TriangleAreaTestCase(unittest.TestCase):
    def test_negative_values(self):
        for _ in range(1000):
            cases = (
                (-random() * randint(1, 1000), random() * randint(1, 1000), random() * randint(1, 1000)),
                (random() * randint(1, 1000), -random() * randint(1, 1000), random() * randint(1, 1000)),
                (random() * randint(1, 1000), random() * randint(1, 1000), -random() * randint(1, 1000)),
                (-random() * randint(1, 1000), -random() * randint(1, 1000), random() * randint(1, 1000)),
                (-random() * randint(1, 1000), random() * randint(1, 1000), -random() * randint(1, 1000)),
                (random() * randint(1, 1000), -random() * randint(1, 1000), -random() * randint(1, 1000)),
                (-random() * randint(1, 1000), -random() * randint(1, 1000), -random() * randint(1, 1000)),
                )
            
            for sides in cases:
                self.assertEqual(get_triangle_area(*sides), -1)
    
    def test_positive_values(self):
        for _ in range(1000):
            sides = (random() * randint(1, 1000), random() * randint(1, 1000), random() * randint(1, 1000))
            p_half = sum(sides) / 2

            area = (p_half * (p_half - sides[0]) * (p_half - sides[1]) * (p_half - sides[2])) ** 0.5
            self.assertEqual(get_triangle_area(*sides), area)
    
    def test_right_triangle_values(self):
        for _ in range(1000):
            side_a = random() * randint(1, 1000)
            side_b = random() * randint(1, 1000)
            side_c = (side_a ** 2 + side_b ** 2) ** 0.5

            area = side_a * side_b / 2 
            self.assertEqual(round(get_triangle_area(side_a, side_b, side_c), 7), round(area, 7))



if __name__ == "__main__":
    unittest.main()
