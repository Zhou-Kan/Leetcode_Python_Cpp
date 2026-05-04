class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

# doubly linked list
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.left, self.tail.right = self.tail, self.head

    def add(self, key: int) -> None:
        node = self.keys[key]
        left = self.head.left
        left.right, node.left = node, left
        self.head.left, node.right = node, self.head

    def remove(self, key: int) -> None:
        node = self.keys[key]
        left, right = node.left, node.right
        left.right, right.left = right, left

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        
        node = self.keys[key]
        self.remove(key)
        self.add(key)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self.remove(key)
            self.add(key)
        else:
            node = Node(key, value)
            self.keys[key] = node
            self.add(key)
            if len(self.keys) > self.capacity:
                last_node = self.tail.right
                self.remove(last_node.key)
                del self.keys[last_node.key]

    def print(self) -> None:
        node = self.tail
        ret = []
        while node:
            ret.append(node.key)
            node = node.right
        print(ret)

test = LRUCache(3)
test.put(0, 0)
test.put(1, 1)
test.put(2, 2)
print(test.print())
test.put(1, 2)
print(test.print())
test.put(3, 2)
print(test.print())
    