import unittest
import hashtable


class HashTableTests(unittest.TestCase):
    def test_put_basic(self):
        h = hashtable.HashTable()
        assert(h.list() == '[]')

        h.put(k=6, v=100)
        h.put(k=1, v=200)
        h.put(k=6, v=300)
        assert(h.list() == '[(1, 200), (6, 300), ]')

        h.put(k=6, v=None)
        assert(h.list() == '[(1, 200), (6, None), ]')

        assert(h.get(0) is None)
        assert(h.get(1) == 200)

    def test_rebalance(self):

        h = hashtable.HashTable()
        for i in range(1999):
            # all elements are under the same key: hash collision
            h.put(i * 5,  i * 5)

        h.rebalance()
        assert len(h) == 1999
