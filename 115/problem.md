# Problem
Given two strings s and t, return the number of distinct 
subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.



### Example 1

Input: s = "rabbbit", t = "rabbit"

Output: 3


### Example 2

Input: s = "babgbag", t = "bag"

Output: 5


# Solution

Thinking about a recursive memoized solution. 

    if the length of t > length of s:
        return 0
    if length of s and t is the same:
        return true if s and t are the same otherwise false
    otherwise:
        if the first character of t and s match:
            check number of subsequent matches betweens[1:] and t[1:]
        check number of subsequence matches between s[1:] and t 

