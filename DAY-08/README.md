# Day 8 - Merge Two Sorted Lists

## Problem

Given two sorted linked lists, merge them into one sorted linked list.

## Example

### Input

list1 = [1,2,4]
list2 = [1,3,4]

### Output

[1,1,2,3,4,4]

## Approach

1. Create a dummy node using `ListNode(0)` to start the result linked list.
2. Set `current = dummy` to track the current position in the result list.
3. Use a `while` loop while both `list1` and `list2` contain nodes.
4. Compare the values of the current nodes of both lists.
5. If `list1.val` is smaller, connect `list1` to `current.next`.
6. Move `list1` to its next node.
7. Move `current` to the newly added node.
8. Otherwise, connect `list2` to `current.next`.
9. Move `list2` to its next node.
10. Move `current` to the newly added node.
11. When one list becomes empty, connect the remaining list directly to the result.
12. Return `dummy.next` because the dummy node is not part of the actual answer.

## Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
