from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('/doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.used = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        node = self.storage.get(key, None)
        # print("GET", node)
        if node != None:
            self.used.move_to_front(node)
            return node.value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        exists = self.storage.get(key, None)
        # print("EXIST", key, exists)
        if exists != None:
            # print("Before", self.used)
            self.used.delete(exists)
            # print("After", self.used)

        new_node = ListNode(value)
        # print("New", new_node)
        self.storage[key] = new_node
        self.used.add_to_head(new_node)

        if self.used.length > self.limit:
            store_keys = list(self.storage.keys())
            store_val = list(self.storage.values())
            del self.storage[store_keys[store_val.index(self.used.tail)]]
            self.used.remove_from_tail()
        # print(self.used)  # self.storage,


# lcache = LRUCache(5)
# lcache.set('first', 5)
# lcache.set('second', 15)
# lcache.set('second', 20)

# print(lcache)
