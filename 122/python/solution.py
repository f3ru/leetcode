


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        
        def helper(start_idx):
            if start_idx+1 >= len(prices):
                return 0
            
            if prices[start_idx] > prices[start_idx + 1]:
                return helper(start_idx + 1)
            else:
                return prices[start_idx + 1] - prices[start_idx ] + helper(start_idx + 1)

        return helper(0)

def test_example1():
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 7
    

def test_example2():
    sol = Solution()
    assert sol.maxProfit([1,2,3,4,5]) == 4
    

def test_example3():
    sol = Solution()
    assert sol.maxProfit([7,6,4,3,1]) == 0