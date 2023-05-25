# Problem

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

### Example 1:

Input: n = 3

Output: 5


### Example 2

Input: n = 1

Output: 1

# Thoughts:

We will have n options for the root value. For each option we need to calculate how many options are available for the left adn right subtrees. 

# Solution

## Recursive 

end condition: if n <= 1: return n

otherwise:
    for each value of n, multiply the number of left siubtrees with the number of right subtrees,
