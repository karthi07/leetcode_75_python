"""
ABCABC ABC

def valid(k):
  if len not divisible return false

  find the muliplier
  n1, n2 = len1 // k, len2 // k
  base = str1[:k]
  return base* n1  = str1 and base * n2 = str2

for i in range(minN, 0, -1)
  if valid(str1[:i]):
    return str1[:i]
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            base = str1[:k]
            n1, n2 = len1 // k, len2 // k
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
