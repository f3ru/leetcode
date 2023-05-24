# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int, min_val: int = 1):
        if n == 1:
            return [TreeNode(min_val)]
        elif n == 0:
            return [None]

        res = []
        for i in range(min_val, min_val + n):
            curr_root_val = i

            left_subtree_min = min_val
            left_subtree_n = i - min_val

            right_subtree_min = i + 1
            right_subtree_n = min_val + n - i - 1

            possible_left_subtrees = self.generateTrees(
                n=left_subtree_n, min_val=left_subtree_min
            )
            possible_right_subtrees = self.generateTrees(
                n=right_subtree_n, min_val=right_subtree_min
            )

            for curr_left_subtree in possible_left_subtrees:
                for curr_right_subtree in possible_right_subtrees:
                    curr_tree = TreeNode(
                        val=curr_root_val,
                        left=curr_left_subtree,
                        right=curr_right_subtree,
                    )
                    res.append(curr_tree)

        return res


sol = Solution()

print(sol.generateTrees(2))
