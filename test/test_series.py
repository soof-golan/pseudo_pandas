import unittest
import pseudo_pandas as pp

class SeriesTestCase(unittest.TestCase):
    def test_happy_path(self):
        my_sr = pp.Series([1, 2, 3], index=['A', 'B', 'C'])
        self.assertEqual(my_sr.loc['B'], 2)
        self.assertEqual(len(my_sr), 3)


if __name__ == '__main__':
    unittest.main()
