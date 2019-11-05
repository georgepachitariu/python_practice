import unittest
import queue

class QueueNodeTests(unittest.TestCase):
    def test_basic(self):
        q = queue.Node(3)
        assert(q.list() == '3 -> None')

        q.add(1)
        q.add(2)
        assert (q.list() == '3 -> 1 -> 2 -> None')

        assert(q.pop() == 3)
        assert(q.list() == '1 -> 2 -> None')
        assert(q.pop() == 1)
        assert(q.list() == '2 -> None')
