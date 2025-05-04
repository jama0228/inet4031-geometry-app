import unittest
import sphere

class SphereTest(unittest.TestCase):

    def test_volume1(self):
        # Test with radius 1
        self.assertAlmostEqual(sphere.volume(1), 4.18879, places=5)

    def test_volume2(self):
        # Test with radius 3
        self.assertAlmostEqual(sphere.volume(3), 113.09734, places=5)

    def test_volume3(self):
        # Test with radius 5
        self.assertAlmostEqual(sphere.volume(5), 523.59878, places=5)

    # Optional failing test example
    # def test_volume_invalid(self):
    #     self.assertNotEqual(sphere.volume(10), 1000)  # Example invalid test

if __name__ == '__main__':
    unittest.main()
