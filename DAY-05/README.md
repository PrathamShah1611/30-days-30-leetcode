# Day 5 - Longest Common Prefix

## Problem

Given an array of strings, find the longest common prefix shared by all strings.

## Example

Input:
strs = ["flower", "flow", "flight"]

Output:
"fl"

Explanation:
"fl" is common at the beginning of all three strings.

## Approach

First, I set `prefix = ""` to store the common prefix.

Then I use a `for` loop to check each character position up to the length of the shortest string.

Inside the loop, I use another `for` loop to check all the other strings.

If any character is different from the first string, I stop the loop.

If all characters are the same, I add the character to `prefix`.

Finally, I return `prefix`.

## Complexity

- Time Complexity: O(n × m)
- Space Complexity: O(1)

## Solution

The solution is available in [`solution.py`](./solution.py).
