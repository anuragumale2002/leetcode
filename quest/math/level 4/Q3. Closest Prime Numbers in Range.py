class Solution:
    def closestPrimes(self, left: int, right: int):
        """
        Ultra-Optimized Prime Range Solution

        ---------------------------------------------------
        PROBLEM
        ---------------------------------------------------
        Find two primes in [left, right] with minimum difference.

        ---------------------------------------------------
        STRATEGY
        ---------------------------------------------------

        1) Generate all primes up to 'right' using Sieve.
        2) Iterate only through primes in range [left, right].
        3) Track smallest difference between consecutive primes.

        ---------------------------------------------------
        WHY SIEVE?
        ---------------------------------------------------

        Checking primality individually:
            O(√n) per number → too slow.

        Sieve gives:
            O(n log log n) total.

        ---------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------

        Sieve: O(right log log right)
        Scan:  O(right)

        ---------------------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------------------

        O(right)

        ---------------------------------------------------
        OPTIMIZATION
        ---------------------------------------------------

        We stop early if difference becomes 1
        (cannot get smaller than 1).
        """

        if right < 2:
            return [-1, -1]

        # Step 1: Sieve
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, right + 1, i):
                    sieve[multiple] = False

        # Step 2: Scan primes in range
        prev_prime = -1
        min_diff = float('inf')
        result = [-1, -1]

        for num in range(max(2, left), right + 1):
            if sieve[num]:
                if prev_prime != -1:
                    diff = num - prev_prime
                    if diff < min_diff:
                        min_diff = diff
                        result = [prev_prime, num]

                        # Minimum possible gap between primes > 2 is 2
                        if min_diff == 1:
                            return result

                prev_prime = num

        return result