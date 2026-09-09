# Day 9 - Remove Duplicates from Sorted Array

## Problem

Given a sorted array, remove the duplicates in-place so that each unique element appears only once.
Return the number of unique elements.

## Example

### Input

nums = [0,0,1,1,1,2,2,3,3,4]

### Output

5

The unique elements are:

[0,1,2,3,4]

## Approach

1. Initialize `i = 0` because the first element is considered unique.
2. Use a `for` loop with `j` starting from index `1` to check the remaining elements.
3. Compare `nums[j]` with `nums[i]`.
4. If `nums[j]` and `nums[i]` are different, a new unique element is found.
5. Increase `i` by `1` to move to the next position for a unique element.
6. Copy `nums[j]` to `nums[i]`.
7. Continue checking all elements using `j`.
8. At the end, `i` represents the index of the last unique element.
9. Return `i + 1` as the total number of unique elements.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
