# Day 4 - Roman to Integer

## Problem

Given a Roman numeral, convert it into an integer.

## Example

Input:
s = "MCMXCIV"

Output:
1994

## Approach

First, I store the values of Roman numerals in a dictionary.

I set `total = 0` to store the answer.

Then I use a `for` loop to go through the Roman numerals one by one.

Inside the loop, I use `if` to compare the current value with the next value.

If the current value is smaller, I subtract it.

Otherwise, I add it.

Finally, I add the value of the last Roman numeral.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
