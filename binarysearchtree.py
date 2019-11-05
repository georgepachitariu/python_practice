
class Node:
    left = None
    right = None

    def __init__(self, val):
        self.val = val

    def add(self, val):
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add(val)

    def list(self):
        l = ''
        r = ''
        if self.left is not None:
            l = self.left.list()
        if self.right is not None:
            r = self.right.list()

        return '(' + l + str(self.val) + r + ')'

    def search(self, val):
        if val == self.val:
            return self

        if val < self.val:
            if self.left is None:
                return None
            else:
                return self.left.search(val)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(val)

    def remove(self):
        if self.left is not None:
            x = self.left  # we go 1 step to the left
            if x.right is None:
                pass # TODO
            while x.right.right is not None:
                x = x.right  # and then all the way to the right
            self.val=x.right.val
            x.right = x.right.left
        else:
            pass # TODO
