"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. 
If the value already exists in the HashMap, update the value.

get(key): Returns the value to which the specified key is mapped, 
or -1 if this map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this 
map contains the mapping for the key.

"""
class Node:
    def __init__(self, key, value):
        # key: int
        # value: int
        self.pair = (key, value)
        self.next = None
        
class MyHashMap:

    # Init array of None with Size
    def __init__(self):
        self.size = 1000
        self.table = [None]*self.size

    # Insert value into the calculated index;
    # append to end of open chain if necessary
    def put(self, key, value):
        # key: int
        # value: int
        index = key % self.size
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            n = self.table[index]
            while True:
                if n.pair[0] == key:
                    n.pair = (key, value)
                    return
                if n.next == None:
                    break
                n = n.next
            f = Node(key, value)
            n.next = f

    # Returns spot in index, iterates to find
    # necessary key if chained
    def get(self, key):
        # key: int
        # return: int
        index = key % self.size
        n = self.table[index]
        while n:
            if n.pair[0] == key:
                return n.pair[1]
            else:
                n = n.next
        return -1
        
    # Remove from index position, 
    # iterate over chain if necessary
    def remove(self, key):
        # key: int
        index = key % self.size
        n = prev = self.table[index]
        if n is None:
            return
        if n.pair[0] == key:
            self.table[index] = n.next
        else:
            n = n.next
            while n:
                if n.pair[0] == key:
                    prev.next = n.next
                    break
                else:
                    n = n.next
                    prev = prev.next
                    
# Runtime: 228 ms, faster than 70.00% of Python3 online submissions for Design HashMap.
# Memory Usage: 16 MB, less than 36.36% of Python3 online submissions for Design HashMap.
if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1,1)
    hashMap.put(2,2)
    print(hashMap.get(1))
    print(hashMap.get(3))
    hashMap.put(2,1)
    print(hashMap.get(2))
    hashMap.remove(2)
    print(hashMap.get(2))