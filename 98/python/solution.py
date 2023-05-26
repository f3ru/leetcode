
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._helper_isValidBST_(root, minRange=float("-inf"), maxRange=float("inf"))
        
    def _helper_isValidBST_(self, root: TreeNode, minRange, maxRange):
        if root == None:
            return True
        
        res = root.val > minRange and root.val < maxRange \
            and self._helper_isValidBST_( root.left, minRange= minRange, maxRange=root.val ) \
            and self._helper_isValidBST_( root.right, minRange= root.val, maxRange=maxRange )
        return res