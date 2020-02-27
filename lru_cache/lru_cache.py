import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.dll = DoublyLinkedList()
        self.limit = limit
        # dictiionary: to save the key,value
        self.dict = dict()
        self.size = 0
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If key-value pair exists in the cache
        if key in self.dict:
            # set the node to the item at the key in dictionary
            # self.dict[key] has the value then node = value
            node = self.dict[key]
            # move the node to end of dll
            self.dll.move_to_end(node)
            # return the nodes value
            # Position0:key, Position1:value
            return node.value[1]
        # otherwise: key-value pair doesn't exist in the cache
        else:
            # return None
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
        # if key exists in storage
        if key in self.dict:
            # set the node to the storage at the key
            node = self.dict[key]
            # set the nodes value to the key value pair
            node.value = (key, value)
            # move the node to the end and 
            self.dll.move_to_end(node)
            return
        
        # if cache is already at max capacity
        elif self.size == self.limit:
            # Remove the oldest entry in the cache
            del self.dict[self.dll.head.value[0]]
            # Remove the node
            self.dll.remove_from_head()
            self.size -= 1
            
        # add a new node (key, value) to the tail (newest entry)
        self.dll.add_to_tail((key, value))
        # set the key in the dictionary
        self.dict[key] = self.dll.tail
        self.size += 1