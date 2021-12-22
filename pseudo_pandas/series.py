import numpy as np
import pandas as pd

class LocHandler:

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, key):
        return self.obj.data[self.obj.index[key]]


class Series:
    def __init__(self, data, index=None):
        if isinstance(data, dict):
            assert index is None
            index = list(data.keys())
            data = [data[k] for k in index]
        if not hasattr(data, '__iter__'):
            if index is None:
                raise ValueError('constant series must not have index')
            data = np.full(len(index), data)
            print(data)
        data = np.array(data)
        self.data = data
        index = index or range(len(self.data))
        self.sliceable_index = index
        self.index = {k: i for i, k in enumerate(index)}

    @property
    def loc(self):
        return LocHandler(self)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return ((i, self.loc[i]) for i in self.index)

    def __repr__(self):
        return '\n'.join(f'{idx}\t{v}' for idx, v in self) + f'\ndtype:{self.data.dtype}'

    def __getitem__(self, i):
        if isinstance(i, slice):
            return Series(self.data[i], self.sliceable_index[i])
        return self.loc[i]

    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
        data_inputs = [x if x is not self else self.data for x in inputs]
        result = getattr(ufunc, method)(*data_inputs, **kwargs)
        if not hasattr(result, "__iter__"):
            return result
        return Series(data=result, index=self.index)

    def __eq__(self, other):
        return all((v == o for v, o in zip(self, other)))