class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Ultra-Optimal Ugly Number Check

        --------------------------------------------------
        CORE IDEA
        --------------------------------------------------

        An ugly number:
            - Is positive
            - Has only prime factors 2, 3, 5

        So if we repeatedly divide by 2, 3, 5
        and end up with 1 → it is ugly.

        --------------------------------------------------
        WHY THIS WORKS
        --------------------------------------------------

        Suppose:
            n = 60

            60 = 2 * 2 * 3 * 5

        Dividing repeatedly:
            60 / 2 = 30
            30 / 2 = 15
            15 / 3 = 5
            5 / 5 = 1

        Ends at 1 → Ugly

        If number had factor 7:
            14 = 2 * 7

            14 / 2 = 7
            Can't divide by 2,3,5 anymore.
            Remains 7 ≠ 1 → Not ugly

        --------------------------------------------------
        EDGE CASE
        --------------------------------------------------

        n <= 0 → Not ugly

        --------------------------------------------------
        TIME COMPLEXITY
        --------------------------------------------------

        O(log n)

        Because each division reduces n significantly.

        --------------------------------------------------
        SPACE COMPLEXITY
        --------------------------------------------------

        O(1)
        """

        if n <= 0:
            return False

        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor

        return n == 1