# Day 6 - Valid Parentheses

## Problem

Given a string containing brackets, check if the brackets are valid.

## Example

Input:
s = "([{}])"

Output:
True

Explanation:
Every opening bracket has the correct closing bracket in the correct order.

## Approach

First, I create an empty stack to store opening brackets.

Then I use a `for` loop to check each bracket one by one.

If the bracket is an opening bracket, I add it to the stack using `append()`.

If it is a closing bracket, I check whether the stack is empty.

Then I remove the last opening bracket using `pop()` and compare it with the current closing bracket.

If they do not match, I return `False`.

Finally, if the stack is empty, I return `True`.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution

The solution is available in [`solution.py`](./solution.py).
