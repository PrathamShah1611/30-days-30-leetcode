# Day 01 — Two Sum

**LeetCode:** Two Sum  
**Difficulty:** Easy  
**Topic:** Array, Hash Map

## Problem

Given an array of integers 'nums' and an integer 'target',
return the indices of the two numbers such that they add up to
'target'.

You may assume that each input has exactly one solution.

## Example

Input:
'nums = [2, 7, 11, 15]'
'target = 9'

Output:
'[0, 1]'

Because:

'2 + 7 = 9'
## Approach

I used two loops to check all possible pairs of numbers.

The first loop selects one number and the second loop selects
another number.

If their sum is equal to the target, I return their indices.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Solution

The solution is available in `solution.py`.
