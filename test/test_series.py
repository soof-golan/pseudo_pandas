import unittest

import numpy as np
import pandas as pd

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

    def test_from_dict(self):
        s = pp.Series({1: 'a', 2: 'b'})
        self.assertEqual(s.loc[1], 'a')

    def test_constant(self):
        s = pp.Series(1, [1, 2, 4])
        self.assertEqual(s.loc[1], 1)
        self.assertEqual(s.loc[2], 1)
        self.assertEqual(s.loc[4], 1)

    def test_slice(self):
        s = pp.Series(np.arange(3), ['A', 'B', 'C'])
        self.assertEqual(list(s[1:3]), [('B', 1), ('C', 2)])

    def test_numpy_funcs(self):
        s = pp.Series(np.arange(3), ['A', 'B', 'C'])
        self.assertEqual(np.sum(s), np.sum(np.arange(3)))
        s = pp.Series(np.arange(-5, 3))
        self.assertEqual(np.sign(s), np.sign(np.arange(-5, 3)))

if __name__ == '__main__':
    unittest.main()
pd.Series