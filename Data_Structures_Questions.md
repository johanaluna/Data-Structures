Answer the following questions for each of the data structures you implemented as part of this project.
https://techdifferences.com/difference-between-array-and-linked-list.html#comments
## Queue

1. What is the runtime complexity of `enqueue`?
O(1) because we don't need to traverse the entire list to set an element in the tail

2. What is the runtime complexity of `dequeue`?
O(1) because we don't need to traverse the entire list to remove an element from the head

3. What is the runtime complexity of `len`?
O(n) because we need to traverse the entire list to count each element

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
O(n)

2. What is the runtime complexity of `contains`?
O(n) -- have to go through from root to the deepest leaf node.

3. What is the runtime complexity of `get_max`? 
O(n) we have to go through every node to figure out maximum
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of
`ListNode.insert_after`?
O(n) go throught the number of nodes in the given Linked List

2. What is the runtime complexity of `ListNode.insert_before`?
O(n) go throught the number of nodes in the given Linked List

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1): replaces the head of the list with a new value


5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1): removes the head node and returns the value stored in it

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1) because we have go just to the tail

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1) because we have go just to the tail

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(n) because have to find that position first

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(n) because have to find that position first

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1) if the position is in the head or tail 
otherwise O(n) because we have to find first the position to delete

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?