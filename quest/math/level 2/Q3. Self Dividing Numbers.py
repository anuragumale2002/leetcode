class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        """
        Ultra-Optimized Self Dividing Numbers

        --------------------------------------------------
        DEFINITION
        --------------------------------------------------

        A number is self-dividing if:
        1) It does NOT contain digit 0.
        2) It is divisible by each of its digits.

        --------------------------------------------------
        STRATEGY
        --------------------------------------------------

        For each number in range [left, right]:

        1) Copy the number to a temporary variable.
        2) Extract digits using:
                digit = temp % 10
                temp //= 10
        3) If:
                digit == 0
                OR number % digit != 0
           → Not self-dividing.

        If all digits pass → add to result.

        --------------------------------------------------
        WHY THIS IS EFFICIENT
        --------------------------------------------------

        - We avoid string conversion.
        - Digit extraction is O(log10(n)).
        - No extra space used.

        --------------------------------------------------
        TIME COMPLEXITY
        --------------------------------------------------

        Let n = right - left
        Each number takes O(d) where d = digits (~log10 n)

        Total: O(n log n)

        --------------------------------------------------
        SPACE COMPLEXITY
        --------------------------------------------------

        O(1) extra space (output excluded)
        """

        res = []

        for num in range(left, right + 1):
            temp = num
            valid = True

            while temp > 0:
                digit = temp % 10

                # If digit is 0 or not divisible
                if digit == 0 or num % digit != 0:
                    valid = False
                    break

                temp //= 10

            if valid:
                res.append(num)

        return res