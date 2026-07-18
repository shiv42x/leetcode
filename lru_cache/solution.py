class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        """
        [left_dummy] <=> [LRU] <=> ... <=> [MRU] <=> [right_dummy]
        """
        self.left_dummy, self.right_dummy = Node(0, 0), Node(0, 0)
        self.left_dummy.next = self.right_dummy
        self.right_dummy.prev = self.left_dummy
    
    # insert node into head of linked list
    def insert(self, node):
        # [existing_node] <=> [right_dummy]
        prev = self.right_dummy.prev
        nxt = self.right_dummy

        prev.next = nxt.prev = node  
        node.next, node.prev = nxt, prev
    
    # remove node from linked list (rewiring pointers)
    def remove(self, node):
        # [] <=> [node] <=> []
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # move self.cache[key] to head of linked list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            lru = self.left_dummy.next
            self.remove(lru)
            del self.cache[lru.key]             

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
