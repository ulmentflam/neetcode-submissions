class Node:
    next: "Node" | None
    prev: "Node" | None
    key: int
    val: int

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    capacity: int
    cache: dict[int, "Node"]
    left: "Node"
    right: "Node"

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: "Node") -> None:
        assert node
        previous, next = node.prev, node.next
        previous.next, next.prev = next, previous

    def _insert(self, node: "Node") -> None:
        assert node
        previous, next = self.right.prev, self.right
        previous.next = next.prev = node
        node.next, node.prev = next, previous

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
        
