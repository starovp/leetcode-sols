"""
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if 
the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

"""
# Node for doubly linked list
class DoubleNode:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:
    # Assign to the cache two nodes for head and tail and a dict
    def __init__(self, capacity):
        self.dict = {}
        self.capacity = capacity
        self.head = DoubleNode(0,0)
        self.tail = DoubleNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # When accessing something in cache, remove (if exists) 
    # and add to right before the tail
    def get(self, key):
        if key in self.dict:
            tnode = self.dict[key]
            self._remove(tnode)
            self._add(tnode)
            return tnode.value
        else:
            return -1

    # When putting something in cache, check for capacity 
    # and then attach to just before the tail
    def put(self, key, value):
        if key in self.dict:
            self._remove(self.dict[key])
            del self.dict[key]

        if len(self.dict) == self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.dict[lru.key]

        newnode = DoubleNode(key, value)
        self.dict[key] = newnode
        self._add(newnode)

    # Add to cache helper function: always adds to just before the tail
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    # Remove node helper: set the previous's next to next 
    # and next's previous to previous
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Runtime: 224 ms, faster than 44.14% of Python3 online submissions for LRU Cache.
# Memory Usage: 22.4 MB, less than 6.06% of Python3 online submissions for LRU Cache.
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))