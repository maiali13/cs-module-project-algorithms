# Find the Smallest Missing Element from a Sorted Array

Given a sorted array of distinct non-negative integers, find the smallest missing element in it.

## Examples

_Input:_ `A = [0, 1, 2, 6, 9, 11, 15]`
_Output:_ The smallest missing element is 3

_Input:_ `A = [1, 2, 3, 4, 6, 9, 11, 15]`
_Output:_ The smallest missing element is 0

_Input:_ `A = [0, 1, 2, 3, 4, 5, 6]`
_Output:_ The smallest missing element is 7


# Find the Middle Node of A Linked List

Write a function that, given a linked list as input, returns the middle node of the linked list. If the linked list contains an even number of nodes, return either of the middle two nodes. 

Our linked list node class looks like this:

```python
class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return f'{self.value}'
```

Example

```python
root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)

root.find_middle()  # should return the Node with value 5
