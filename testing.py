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
