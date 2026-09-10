# Day 10 - Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.
Return the number of elements in `nums` that are not equal to `val`.

## Example

### Input

nums = [3,2,2,3]
val = 3

### Output

2

### Explanation

The value `3` is removed.

The remaining elements are:
[2,2]

## Approach

1. Initialize `i = 0` to track the position where the next valid element should be placed.
2. Use a `for` loop with `j` to check every element of the array.
3. Check if `nums[j]` is not equal to `val`.
4. If the element is not equal to `val`, it is a valid element.
5. Copy the valid element to position `i` using `nums[i] = nums[j]`.
6. Increase `i` by 1 to move to the next position.
7. If `nums[j]` is equal to `val`, skip it and continue checking the next element.
8. After checking all elements, return `i`.
9. `i` represents the number of elements that are not equal to `val`.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
