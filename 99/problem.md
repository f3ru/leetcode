# Problem

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.





# Solution


# Resursive with min and max node pointers

Similar solution as 98, but we need to keep track of the min and max pointers. Swapping the values when we find a mismatch should give us the solution.