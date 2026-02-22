class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        Ultra-Optimized DP Solution

        -------------------------------------------------------
        KEY RECURRENCE
        -------------------------------------------------------

        dp[n][k] = dp[n-1][k-1] + (n-1) * dp[n-1][k]

        Explanation:

        When inserting tallest stick:

        1) If placed at front:
           → increases visible count by 1
           → dp[n-1][k-1]

        2) If placed in any of remaining (n-1) positions:
           → visible count unchanged
           → (n-1) * dp[n-1][k]

        -------------------------------------------------------
        TIME COMPLEXITY
        -------------------------------------------------------

        O(n*k)

        -------------------------------------------------------
        SPACE COMPLEXITY
        -------------------------------------------------------

        O(k)   (1D rolling array)

        -------------------------------------------------------
        MODULO
        -------------------------------------------------------

        Required to avoid overflow.
        """

        MOD = 10**9 + 7

        # dp[j] represents dp[current_n][j]
        dp = [0] * (k + 1)
        dp[0] = 1  # Base case

        for sticks in range(1, n + 1):
            new_dp = [0] * (k + 1)

            for visible in range(1, min(sticks, k) + 1):
                new_dp[visible] = (
                    dp[visible - 1] +
                    (sticks - 1) * dp[visible]
                ) % MOD

            dp = new_dp

        return dp[k]