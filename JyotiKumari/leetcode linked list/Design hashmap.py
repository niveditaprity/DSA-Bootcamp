class LL_Node:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:

    def __init__(self):
        self.hashmap = [None] * 10000

    def put(self, key: int, value: int) -> None:
        keyy = key % 10000
        if self.hashmap[keyy] is None:
            self.hashmap[keyy] = LL_Node(key, value)
        else:
            node = self.hashmap[keyy]
            while node:
                if node.key == key:
                    node.val = value
                    return
                node = node.next
            node = self.hashmap[keyy]
            self.hashmap[keyy] = LL_Node(key, value, node)
            
    def get(self, key: int) -> int:
        keyy = key % 10000
        if self.hashmap[keyy] is None:
            return -1
        else:
            node = self.hashmap[keyy]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
            return -1

    def remove(self, key: int) -> None:
        keyy = key % 10000
        if self.hashmap[keyy]:
            node = self.hashmap[keyy]
            if node.key == key:
                self.hashmap[keyy] = node.next
                return 
            prev = node
            node = node.next
            while node:
                if node.key == key:
                    prev.next = node.next
                    return 
                prev = prev.next
                node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)