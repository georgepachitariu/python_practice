import unittest
import stack

class StackNodeTests(unittest.TestCase):
    def test_basic(self):
        q = stack.Node(3)
        assert(q.list() == '3 -> None')

        q.push(1)
        q.push(2)
        assert (q.list() == '2 -> 1 -> 3 -> None')

        assert(q.pop() == 2)
        assert(q.list() == '1 -> 3 -> None')
        assert(q.pop() == 1)
        assert(q.list() == '3 -> None')
