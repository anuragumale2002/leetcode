class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Ultra-Optimized Factorial Trailing Zeroes

        ---------------------------------------------------
        CORE IDEA
        ---------------------------------------------------

        Trailing zero comes from factor 10.
        And:
            10 = 2 × 5

        In factorial, there are more 2s than 5s.
        So trailing zero count = number of 5s in n!

        ---------------------------------------------------
        HOW TO COUNT 5s
        ---------------------------------------------------

        Count:
            n//5      (multiples of 5)
            n//25     (extra 5s from 25, 50, 75...)
            n//125    (extra 5s from 125, 250...)
            ...

        Keep dividing by 5 until zero.

        ---------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------

        O(log₅ n)

        Because n is divided by 5 each iteration.

        ---------------------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------------------

        O(1)

        ---------------------------------------------------
        WHY THIS IS OPTIMAL
        ---------------------------------------------------

        Any solution must at least examine powers of 5.
        This is mathematically minimal.
        """

        count = 0

        while n > 0:
            n //= 5
            count += n

        return count