class ListNode:

    def __init__(self, value, prev=None, next_node=None):
        self.value = value
        self.prev = prev
        self.next = next_node

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev


    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        if not self.head and not self.tail:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        if self.head == None:
            return None
        max_node = self.head.value
        actual_node = self.head
        while actual_node:
            if actual_node.value > max_node:
                max_node = actual_node.value
            actual_node = actual_node.next
        return max_node