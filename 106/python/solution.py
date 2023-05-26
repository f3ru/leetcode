# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        # Empty tree
        if inorder == []:
            return None

        root_val = postorder[-1]
        num_items_left_subtree = inorder.index(root_val)

        left_subtree = self.buildTree(
            inorder=inorder[:num_items_left_subtree],
            postorder=postorder[:num_items_left_subtree],
        )
        right_subtree = self.buildTree(
            inorder=inorder[num_items_left_subtree + 1:],
            postorder=postorder[num_items_left_subtree:-1],
        )

        return TreeNode(root_val, left_subtree, right_subtree)
