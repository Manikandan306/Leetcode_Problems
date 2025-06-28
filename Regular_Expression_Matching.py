class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Initialize dp for patterns like a*, a*b*, a*b*c* etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Two cases:
                    # 1. Use 0 of the preceding char → dp[i][j - 2]
                    # 2. Use 1+ of the preceding char → dp[i - 1][j]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]

        return dp[m][n]