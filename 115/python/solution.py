import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # solution here
        self.s = s
        self.t = t
        self.len_s = len(s)
        self.len_t = len(t)
        return self._numDistinctIdx_(0, 0)
    
    @functools.lru_cache(maxsize=1000)
    def _numDistinctIdx_(self, s_idx, t_idx):
        if s_idx >= self.len_s  or (self.len_s - s_idx ) < (self.len_t - t_idx):
            return 0
        elif t_idx >= self.len_t:
            return 1
        # elif t_idx == (self.len_t -1):
        #     return 1 if self.s[s_idx] == self.t[t_idx] else 0
        elif (self.len_s - s_idx ) == (self.len_t - t_idx) and (self.len_s - s_idx ) == 1:
            return 1 if self.s[s_idx:] == self.t[t_idx:] else 0
        
        res = 0
        if self.s[s_idx] == self.t[t_idx]:
            res += self._numDistinctIdx_(s_idx+1, t_idx+1)
        
        res += self._numDistinctIdx_(s_idx+1, t_idx)
        print(s_idx, t_idx, res)
        return res
    

def test_ex1():
    sol = Solution()
    s = "rabbbit"
    t = "rabbit"
    assert sol.numDistinct(s,t) == 3


def test_ex2():
    sol = Solution()
    s = "babgbag"
    t = "bag"
    assert sol.numDistinct(s,t) == 5
    

def test_ex2():
    sol = Solution()
    s = "babgbag"
    t = "bag"
    assert sol.numDistinct(s,t) == 5
