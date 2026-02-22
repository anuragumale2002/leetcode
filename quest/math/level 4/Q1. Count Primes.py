class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Ultra-Optimized Sieve of Eratosthenes

        -----------------------------------------------------
        PROBLEM
        -----------------------------------------------------
        Count prime numbers strictly less than n.

        -----------------------------------------------------
        CORE IDEA
        -----------------------------------------------------
        Use Sieve of Eratosthenes:

        1. Create boolean array is_prime of size n.
        2. Initialize all entries as True except 0 and 1.
        3. For each number i from 2 to sqrt(n):
              If i is prime:
                  Mark all multiples of i starting from i*i as False.

        Why start from i*i?
            Because smaller multiples were already marked
            by smaller primes.

        -----------------------------------------------------
        TIME COMPLEXITY
        -----------------------------------------------------
        O(n log log n)

        This is mathematically proven complexity
        of the Sieve of Eratosthenes.

        -----------------------------------------------------
        SPACE COMPLEXITY
        -----------------------------------------------------
        O(n)

        -----------------------------------------------------
        WHY THIS IS OPTIMAL
        -----------------------------------------------------
        Any algorithm that lists primes up to n
        must at least touch n numbers.
        So O(n log log n) is near optimal.
        """

        if n <= 2:
            return 0

        # Boolean array
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Only need to check up to sqrt(n)
        limit = int(n ** 0.5) + 1

        for i in range(2, limit):
            if is_prime[i]:
                # Start marking from i*i
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = False

        return sum(is_prime)