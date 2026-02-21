class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        General solution without hardcoded primes.

        Approach:
        - Count set bits using bit_count()
        - Check primality using sqrt(n) check

        Time Complexity: O(N * sqrt(M))
        Where:
            N = right - left + 1
            M = max bit count (<= 64 typically)
        
        Space Complexity: O(1)
        """

        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        count = 0

        for num in range(left, right + 1):
            if is_prime(num.bit_count()):
                count += 1

        return count
