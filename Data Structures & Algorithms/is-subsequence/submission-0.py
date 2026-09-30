class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return rec(i + 1, j + 1)
            return rec(i, j + 1)
        return rec(0, 0)