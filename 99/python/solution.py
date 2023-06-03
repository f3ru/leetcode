
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def recoverTree(self, root: TreeNode) -> bool:
        minRange = TreeNode("-inf")
        maxRange = TreeNode("inf")
        self._helper_recoverTree_(root, minRange=minRange, maxRange=maxRange)
        
    def _helper_recoverTree_(self, root: TreeNode, minRange: TreeNode, maxRange: TreeNode) -> None:
        if root == None:
            return 
        
        if root.val < minRange.val:
            temp = root.val
            root.val = minRange.val
            minRange.val = temp
        elif root.val < maxRange.val:
            temp = root.val
            root.val = maxRange.val
            maxRange.val = temp
        else:
            self._helper_isValidBST_( root.left, minRange= minRange, maxRange=root )
            self._helper_isValidBST_( root.right, minRange= root, maxRange=maxRange )
        