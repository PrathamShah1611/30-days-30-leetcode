# Day 7 - Add Two Numbers

## Problem

Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the sum as a linked list.
The digits are stored in reverse order.

## Example

Input:
l1 = [2,4,3]
l2 = [5,6,4]

Output:
[7,0,8]

Explanation:
342 + 465 = 807

## Approach

1. Initialize `carry = 0` to store the carry value from addition.
2. Create a dummy node using `ListNode(0)` to start the result linked list.
3. Set `current = dummy` to keep track of the current position in the result list.
4. Use a `while` loop that continues while `l1`, `l2`, or `carry` exists.
5. Get the value of the current node of `l1`. If `l1` is empty, use `0`.
6. Get the value of the current node of `l2`. If `l2` is empty, use `0`.
7. Add both values along with the carry and store the result in `total`.
8. Use `total % 10` to get the digit that should be stored in the current result node.
9. Use `total // 10` to calculate the carry for the next addition.
10. Create a new `ListNode` using the calculated digit and connect it to the result list.
11. Move `current` to the newly created node.
12. Move `l1` and `l2` to their next nodes if they exist.
13. Continue the loop until both linked lists are finished and there is no remaining carry.
14. Return `dummy.next` because the dummy node is only used as the starting point of the result list.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution

The solution is available in [`solution.py`](./solution.py).
