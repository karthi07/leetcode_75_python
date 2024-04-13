"""
"ace" is a subsequence of "abcde" while "aec" is not
ptr  = 1
abcde
ace
----


bcde
ce
---
ptr = 2

de
e
---

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matchingCount = 0
        if not s:
            return True
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if s[matchingCount] == t[i]:
                matchingCount += 1
            if matchingCount == len(s):
                return True
        return False
