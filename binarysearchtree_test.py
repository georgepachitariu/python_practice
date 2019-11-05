import unittest
import binarysearchtree


class BinarySearchTreeTests(unittest.TestCase):
    def test_basic(self):
        t = binarysearchtree.Node(10)
        assert(t.list() == '(10)')

        t.add(5)
        t.add(7)
        t.add(6)
        assert(t.list() == '((5((6)7))10)')

        assert(t.search(7) is not None)
        assert(t.search(8) is None)

        t.search(10).remove()
        assert(t.list() == '((5(6))7)')
