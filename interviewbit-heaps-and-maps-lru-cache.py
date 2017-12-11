class LRUCache:
    class DLLNode:
        def __init__(self, val=None):
            self.val = val
            self.prev = None
            self.next = None

    class DLL:
        def __init__(self):
            self.head = None
            self.tail = None

    def update_index(self, the_key):
        if self.cache[the_key][1] != self.index.tail:
            if self.cache[the_key][1] == self.index.head:
                self.index.head = self.cache[the_key][1].next
                self.index.head.prev = None
            else:
                self.cache[the_key][1].prev.next = self.cache[the_key][1].next
                self.cache[the_key][1].next.prev = self.cache[the_key][1].prev

            self.index.tail.next = self.cache[the_key][1]
            self.cache[the_key][1].prev = self.index.tail
            self.index.tail = self.cache[the_key][1]
            self.cache[the_key][1].next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.index = self.DLL()

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.update_index(key)
            return self.cache[key][0]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache[key][0] = value
            self.update_index(key)
        else:
            new_node = self.DLLNode(key)
            if len(self.cache) < self.capacity:
                if  not self.index.head:
                    self.index.head = new_node
                    self.index.tail = new_node
                else:
                    self.index.tail.next = new_node
                    new_node.prev = self.index.tail
                    self.index.tail = new_node
            else:
                del self.cache[self.index.head.val]
                if self.capacity == 1:
                    self.index.head = new_node
                    self.index.tail = new_node
                else:
                    self.index.head = self.index.head.next
                    self.index.head.prev = None
                    new_node.prev = self.index.tail
                    self.index.tail.next = new_node
                    self.index.tail = new_node
            self.cache[key] = [value, new_node]
