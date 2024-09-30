class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.count = 0


class AllOne:

    def __init__(self):
        # Create doubly-linked list
        self.root = DoubleNode(None)
        self.root.next = self.root
        self.root.prev = self.root
        # Create map to elements
        self.elems = {}

    def inc(self, key: str) -> None:
        if key not in self.elems:
            node = DoubleNode(key)
            self.elems[key] = node
            node.count = 1
            node.next = self.root.next
            node.next.prev = node
            self.root.next = node
            node.prev = self.root
        else:
            node = self.elems[key]
            node.count += 1
            while node.next is not self.root and node.next.count < node.count:
                a, b, c, d = node.prev, node, node.next, node.next.next
                a.next, c.next, b.next = c, b, d
                d.prev, b.prev, c.prev = b, c, a

    def dec(self, key: str) -> None:
        node = self.elems[key]
        if node.count == 1:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.count = 0
            del node
            del self.elems[key]
        else:
            node.count -= 1
            while node.prev is not self.root and node.prev.count > node.count:
                a, b, c, d = node.prev.prev, node.prev, node, node.next
                a.next, c.next, b.next = c, b, d
                d.prev, b.prev, c.prev = b, c, a

    def getMaxKey(self) -> str:
        if self.root.prev != self.root:
            return self.root.prev.val
        else:
            return ""
        

    def getMinKey(self) -> str:
        if self.root.next != self.root:
            return self.root.next.val
        else:
            return ""
