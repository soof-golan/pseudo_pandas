import unittest

import numpy as np

import pseudo_pandas as pp


class SeriesTestCase(unittest.TestCase):
    def test_happy_path(self):
        my_sr = pp.Series([1, 2, 3], index=['A', 'B', 'C'])
        self.assertEqual(my_sr.loc['B'], 2)
        self.assertEqual(len(my_sr), 3)

    def test_numpy_data(self):
        my_sr = pp.Series(np.array([1, 2, 3]), index=['A', 'B', 'C'])
        self.assertEqual(my_sr.loc['B'], 2)
        self.assertEqual(len(my_sr), 3)

    def test_auto_index(self):
        my_sr = pp.Series(np.array([1, 2, 3]))
        self.assertEqual(my_sr.loc[1], 2)
        self.assertEqual(len(my_sr), 3)

    def test_repr(self):
        my_sr = pp.Series(np.array([1, 2, 3]))
        self.assertEqual(repr(my_sr), """0\t1\n1\t2\n2\t3\ndtype:int32""")



if __name__ == '__main__':
    unittest.main()
