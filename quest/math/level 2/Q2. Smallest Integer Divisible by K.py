class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Ultra-Optimized Modular Arithmetic Solution

        ------------------------------------------------
        CORE IDEA
        ------------------------------------------------

        We need the smallest number consisting only of digit '1'
        that is divisible by k.

        Instead of building huge numbers, we track only remainders.

        If:
            current remainder = r
        Then next remainder:
            (r * 10 + 1) % k

        If remainder becomes 0 → number divisible.

        ------------------------------------------------
        IMPORTANT OBSERVATION
        ------------------------------------------------

        If k is divisible by 2 or 5:
            Return -1

        Because numbers made of only 1's:
            1, 11, 111, ...
        never end in 0 or even number.

        So they can never be divisible by 2 or 5.

        ------------------------------------------------
        WHY WE WON'T LOOP FOREVER
        ------------------------------------------------

        There are only k possible remainders:
            0,1,2,...,k-1

        If we don't get remainder 0 within k steps,
        a cycle must repeat.

        So maximum iterations = k.

        ------------------------------------------------
        TIME COMPLEXITY
        ------------------------------------------------

        O(k)

        ------------------------------------------------
        SPACE COMPLEXITY
        ------------------------------------------------

        O(1)
        """

        # Impossible cases
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0

        # At most k iterations (Pigeonhole principle)
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1