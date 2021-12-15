import numpy as np


class LocHandler:

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, key):
        return self.obj.data[self.obj.index[key]]


class Series:
    def __init__(self, data, index=None):
        self.data = np.array(data)
        index = index or range(len(self.data))
        self.index = {k: i for i, k in enumerate(index)}

    @property
    def loc(self):
        return LocHandler(self)

    def __len__(self):
        return len(self.data)