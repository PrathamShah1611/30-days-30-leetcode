# Day 2 - Best Time to Buy and Sell Stock

## Problem

Given an array of prices, find the maximum profit that can be made by buying on one day and selling on a later day.

## Approach

First, I tried using two loops to check every possible buy and sell pair.
It worked, but it was too slow for large inputs.

So, I improved the approach by using only one loop.

First, I set the first price as the minimum price.
Then I check each price one by one.
If I find a lower price, I update the minimum price.
Then I calculate the profit using the current price and minimum price.
If the profit is greater than the maximum profit, I update the maximum profit.
Finally, I return the maximum profit.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)
