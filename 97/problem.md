# Problem

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



### Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

Output: true

Explanation: One way to obtain s3 is:

Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".

Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

Since s3 can be obtained by interleaving s1 and s2, we return true.


### Example 2


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"

Output: false

Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

### Example 3

Input: s1 = "", s2 = "", s3 = ""
Output: true


# Thoughts:

three pointer?

there are multiple paths we need to explore 

# Solution


# three pointer

create a helper function that takes in the starting position of each string and returns whether the s3 substring can be formed using the substring from s1 and s3

Main function: 

    return false if sorted s3 != sorted s1 + s2

Helper function:

    if current char of s3 != s1 or s2: return false
    if current char of s3 == s1 and s2: return helper function with two recursive calls
    if current char of s3 == s1 and not s2: return helper function with a recursive calls (s3 + 1, s1+1)
    if current char of s3 == s2 and not s1: return helper function with a recursive calls (s3 + 1, s2+1)
    