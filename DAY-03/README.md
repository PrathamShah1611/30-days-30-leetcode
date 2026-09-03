# Day 3 - Palindrome Number

## Problem

Given an integer x, return `true` if `x` is a palindrome, and `false` otherwise.

## Example

Input:
x = 121

Output:
True

Explanation:
121 reads the same forward and backward.

## Approach

First, I save the original number.

Then I take the last digit of the number using `% 10`.

I add the digit to the reverse number.

Then I remove the last digit using `// 10`.

I repeat this until the number becomes 0.

Finally, I compare the original number with the reverse number.

If both are the same, I return `true`. Otherwise, I return `false`.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
