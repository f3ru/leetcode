import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if sorted(s3) != sorted(s1 + s2):
            return False

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

        return self.__isInterLeaveSubStr__(0, 0, 0)

    @functools.lru_cache(maxsize=400)
    def __isInterLeaveSubStr__(self, i1: int, i2: int, i3: int) -> bool:
        print(i1, i2, i3)
        # End conditions
        if i3 == len(self.s3):
            return True
        elif i2 == len(self.s2):
            return self.s3[i3:] == self.s1[i1:]
        elif i1 == len(self.s1):
            return self.s3[i3:] == self.s2[i2:]

        # Recursive condition
        if self.s3[i3] == self.s1[i1]:
            return self.__isInterLeaveSubStr__(i1 + 1, i2, i3 + 1) or (
                self.s3[i3] == self.s2[i2]
                and self.__isInterLeaveSubStr__(i1, i2 + 1, i3 + 1)
            )
        elif self.s3[i3] == self.s2[i2]:
            return self.__isInterLeaveSubStr__(i1, i2 + 1, i3 + 1)
        else:
            return False


def test_isInterleaf1():
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert sol.isInterleave(s1, s2, s3)


def test_isInterleaf2():
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    assert not sol.isInterleave(s1, s2, s3)


def test_isInterleaf3():
    sol = Solution()
    s1 = ""
    s2 = ""
    s3 = ""
    assert sol.isInterleave(s1, s2, s3)
