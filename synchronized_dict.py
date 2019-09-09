# MIT License
#
# Copyright (c) 2019 Weston Berg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''
Module providing primitive, synchronized dictionary-like structure
with thread safe access.
'''
import collections
from threading import RLock


class SynchronizedDict(collections.MutableMapping):
    '''
    Class representing simple, synchronized dictionary
    '''
    def __init__(self, *args, **kwargs):
        self._map = dict()       # Structure for storing data
        self.update(dict(*args, **kwargs))
        self._lock = RLock()     # Access lock

    @classmethod
    def fromkeys(cls, iterable, value=None):
        sync_dict = SynchronizedDict()

        sync_dict._map = dict.fromkeys(iterable, value)

        return sync_dict

    def __getitem__(self, key):
        with self._lock:
            item = self._map[key]

        return item

    def __setitem__(self, key, value):
        with self._lock:
            self._map[key] = value

    def __delitem__(self, key):
        with self._lock:
            del self._map[key]

    def __iter__(self):
        with self._lock:
            it = iter(self._map)

        return it

    def __len__(self):
        with self._lock:
            length = len(self._map)

        return length

    def __str__(self):
        with self._lock:
            s = str(self._map)

        return s
