import functools


class Solution:
    @functools.lru_cache(maxsize=100)
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for left_tree_size in range(0, n):
            possible_left_subtrees = self.numTrees(left_tree_size)

            right_tree_size = n-left_tree_size-1
            possible_right_subtrees = self.numTrees(right_tree_size)

            res += possible_left_subtrees*possible_right_subtrees

        return res


def test_numTrees():
    sol = Solution()
    assert sol.numTrees(3) == 5
    assert sol.numTrees(1) == 1
