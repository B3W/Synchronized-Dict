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
Testing module
'''
import synchronized_dict
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    def thread_func(d, iterable):
        '''
        d = dict
        iterable = key/value pairs
        '''
        for key, value in iterable.items():
            d[key] = value

    sd = synchronized_dict.SynchronizedDict()

    # Key/value pairs with some conflicts
    it1 = {1: 1, 2: 2, 3: 3, 9: 9, 10: 11}
    it2 = {6: 7, 7: 7, 8: 9, 9: 9, 10: 10}
    it3 = {6: 6, 7: 8, 8: 8, 4: 4, 5: 5}

    # for key, value in it1.items():
    #     print('%d: %d' % (key, value))

    with ThreadPoolExecutor() as executor:
        executor.submit(thread_func, sd, it3)
        executor.submit(thread_func, sd, it1)
        executor.submit(thread_func, sd, it2)

    # keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # sd = synchronized_dict.SynchronizedDict.fromkeys(keys, 800)

    print(sd)
