
class Node:
    next = None

    def __init__(self, val):
        self.val = val

    "To add the first elem. run only the constructor"
    def push(self, val):
        if self.next is None:
            self.next = Node(self.val)
            self.val = val
        else:
            # we add a new node on the second position
            new_node = Node(self.val)
            new_node.next = self.next

            self.val=val
            self.next=new_node

    def list(self):
        s = str(self.val) + ' -> '
        if self.next is None:
            s += 'None'
        else:
            s += self.next.list()
        return s

    """If there is only 1 element, it cannot be removed"""
    def pop(self):
        result = self.val
        if self.next is None:
            raise Exception('We cannot remove an element if'
                            'the last one')
        # we copy over the value from the next node
        self.val=self.next.val
        # and then we skip the next node
        self.next=self.next.next

        return result