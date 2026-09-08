class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if key in self.data:
            self.remove(self.data[key])
            self.insert(self.data[key])
            return self.data[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(self.data[key])
        self.data[key] = Node(key, value)
        self.insert(self.data[key])

        if len(self.data) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.data[lru.key]
        
