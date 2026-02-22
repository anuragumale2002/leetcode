class Solution:
    def generate(self, numRows: int):
        """
        Ultra-Optimized Pascal's Triangle

        ------------------------------------------------
        CORE IDEA
        ------------------------------------------------

        Pascal's identity:
            C(n, k) = C(n-1, k-1) + C(n-1, k)

        So each element (except edges) is:
            previous_row[j-1] + previous_row[j]

        ------------------------------------------------
        WHY THIS IS OPTIMAL
        ------------------------------------------------

        - We avoid factorial computation.
        - We build each row using the previous row.
        - Each element is computed exactly once.

        ------------------------------------------------
        TIME COMPLEXITY
        ------------------------------------------------

        Total elements generated:
            1 + 2 + 3 + ... + n
            = n(n+1)/2

        So complexity:
            O(n²)

        This is optimal because output size itself is O(n²).

        ------------------------------------------------
        SPACE COMPLEXITY
        ------------------------------------------------

        O(n²) for storing result.
        """

        if numRows <= 0:
            return []

        triangle = [[1]]  # First row

        for i in range(1, numRows):
            prev_row = triangle[-1]

            # Start row with 1
            new_row = [1]

            # Compute middle values
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            # End row with 1
            new_row.append(1)

            triangle.append(new_row)

        return triangle