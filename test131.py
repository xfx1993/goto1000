class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.length = 0
        self.helper = dict()
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.helper:
            k, v = self.helper[key].val
            return v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.head:
            self.head = ListNode((key, value))
            self.length += 1
            self.helper[key] = self.head
            self.tail = self.head
        else:
            if key in self.helper:
                node = self.helper[key]
                k, v = node.val
                self.helper[key].val = (key, value)
            else:
                if self.length < self.capacity:
                    cur = ListNode((key, value))
                    self.tail.next = cur
                    cur.pre = self.tail
                    self.tail = cur
                    self.length += 1
                    self.helper[key] = cur
                else:
                    k, v = self.head.val
                    del self.helper[k]
                    self.head = self.head.next
                    self.head.pre = None

                    cur = ListNode((key, value))
                    self.tail.next = cur
                    cur.pre = self.tail
                    self.tail = cur
                    self.helper[key] = cur

cache = LRUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
