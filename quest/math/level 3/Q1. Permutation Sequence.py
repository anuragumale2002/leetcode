class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Ultra-Optimized Factorial Number System Solution

        ---------------------------------------------------
        CORE IDEA
        ---------------------------------------------------

        Total permutations of n numbers = n!

        Each digit position changes every (n-1)! permutations.

        Example:
            n = 4
            Total = 24

            First digit repeats every 6 permutations:
            1xxxx → 6 perms
            2xxxx → 6 perms
            3xxxx → 6 perms
            4xxxx → 6 perms

        So to find k-th permutation:
            - Determine which block of size (n-1)! it belongs to.
            - Select corresponding digit.
            - Reduce problem size by 1.

        ---------------------------------------------------
        IMPORTANT DETAIL
        ---------------------------------------------------

        Convert k to zero-based index:
            k -= 1

        Because factorial indexing is zero-based.

        ---------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------

        O(n^2)

        Why?
            Removing elements from list costs O(n)
            Done n times.

        Since n ≤ 9 (constraint), this is optimal.

        ---------------------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------------------

        O(n)
        """

        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Available numbers
        numbers = list(map(str, range(1, n + 1)))

        k -= 1  # convert to zero-based index

        result = []

        for i in range(n, 0, -1):
            block_size = factorial[i - 1]

            index = k // block_size
            result.append(numbers[index])

            # Remove used number
            numbers.pop(index)

            k %= block_size

        return "".join(result)