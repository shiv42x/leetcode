from collections import defaultdict

class CacheEntry:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.counter = 1

class DoublyLinkedListNode:
    def __init__(self, cache_entry: CacheEntry):
        self.prev = None
        self.next = None
        self.cache_entry = cache_entry

class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = DoublyLinkedListNode(CacheEntry(0, 0))
        self.tail = DoublyLinkedListNode(CacheEntry(0, 0))

        # head <=> tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node: DoublyLinkedListNode):
        old_node = self.tail.prev
        old_node.next = node
        node.prev = old_node
        node.next = self.tail
        self.tail.prev = node
        self.length += 1

    def prepend(self, node: DoublyLinkedListNode):
        old_node = self.head.next
        old_node.prev = node
        node.next = old_node
        self.head.next = node
        node.prev = self.head
        self.length += 1

    def remove(self, node: DoublyLinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.frequency = defaultdict(DoublyLinkedList)
        self.data = {}  # maps key -> DoublyLinkedListNode

    def _update_node_frequency(self, node: DoublyLinkedListNode):
        old_freq = node.cache_entry.counter
        new_freq = old_freq + 1
        node.cache_entry.counter = new_freq

        self.frequency[old_freq].remove(node)

        if old_freq == self.min_freq and self.frequency[old_freq].length == 0:
            self.min_freq += 1

        self.frequency[new_freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        node = self.data[key]
        self._update_node_frequency(node)
        return node.cache_entry.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # key already exists, update value and shift frequency
        if key in self.data:
            node = self.data[key]
            node.cache_entry.val = value
            self._update_node_frequency(node)
            return

        # capacity full, evict the LFU/LRU item
        if len(self.data) == self.capacity:
            # head of our DLL stores the least-recently used items of that frequency
            lfu_list = self.frequency[self.min_freq]
            evict_node = lfu_list.head.next  # least recently used item
            
            lfu_list.remove(evict_node)
            del self.data[evict_node.cache_entry.key]

        entrant = CacheEntry(key, value)
        node = DoublyLinkedListNode(entrant)

        self.data[key] = node
        self.min_freq = 1  
        self.frequency[1].append(node)