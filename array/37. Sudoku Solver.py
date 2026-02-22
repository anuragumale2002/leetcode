from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Ultra-Optimized Sudoku Solver

        ---------------------------------------
        WHY THIS IS FASTER THAN NORMAL VERSION
        ---------------------------------------

        1) We use BITMASKING instead of sets.
           - Each row/col/box is represented as a 9-bit integer.
           - Bit i (1<<i) means digit i is already used.
           - Checking validity becomes O(1) using bit operations.
           - Bit operations are significantly faster than set lookups.

        2) We use MRV (Minimum Remaining Values) heuristic.
           - Instead of filling empty cells sequentially,
             we always choose the cell with the fewest valid options.
           - This reduces branching drastically.
           - Fewer recursive calls → much faster solving.

        3) We iterate only over VALID numbers using bit tricks:
           - available_mask gives all possible digits.
           - We extract one valid digit at a time using:
                pick = mask & -mask
           - This extracts the rightmost set bit efficiently.

        ---------------------------------------
        WHAT EACH DATA STRUCTURE STORES
        ---------------------------------------

        rows[i]  -> bitmask of digits used in row i
        cols[j]  -> bitmask of digits used in column j
        boxes[k] -> bitmask of digits used in box k

        Example:
            If row[0] = 0b000101010
            It means digits corresponding to set bits are already used.

        Digit to bit mapping:
            digit '1' -> bit 1 (1 << 1)
            digit '2' -> bit 2 (1 << 2)
            ...
            digit '9' -> bit 9 (1 << 9)

        ---------------------------------------
        TIME COMPLEXITY
        ---------------------------------------
        Worst-case: O(9^m), m = empty cells
        But MRV + pruning makes it extremely fast in practice.

        ---------------------------------------
        SPACE COMPLEXITY
        ---------------------------------------
        O(1) extra space (fixed 9x9 board)
        Recursion depth <= 81
        """

        # Bitmasks for rows, columns, and boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        empty = []

        # Initialize masks
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    digit = int(board[r][c])
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + (c // 3)] |= mask

        def backtrack():
            # If no empty cells left, solved
            if not empty:
                return True

            # ---------------------------------------
            # MRV: choose cell with fewest options
            # ---------------------------------------
            min_options = 10
            min_index = -1

            for i in range(len(empty)):
                r, c = empty[i]
                box_index = (r // 3) * 3 + (c // 3)

                # Bits that are already used
                used = rows[r] | cols[c] | boxes[box_index]

                # Available digits = inverse of used (only bits 1–9)
                available = (~used) & 0x3FE  # 0x3FE = binary 1111111110

                count = bin(available).count('1')

                if count < min_options:
                    min_options = count
                    min_index = i

                if count == 1:
                    break

            # If no possible number → dead end
            if min_options == 0:
                return False

            # Swap chosen cell to end for easy pop
            empty[min_index], empty[-1] = empty[-1], empty[min_index]
            r, c = empty.pop()
            box_index = (r // 3) * 3 + (c // 3)

            used = rows[r] | cols[c] | boxes[box_index]
            available = (~used) & 0x3FE

            # Try each valid number using bit trick
            while available:
                pick = available & -available  # extract rightmost set bit
                digit = pick.bit_length() - 1

                # Place digit
                board[r][c] = str(digit)
                rows[r] |= pick
                cols[c] |= pick
                boxes[box_index] |= pick

                if backtrack():
                    return True

                # Undo (backtrack)
                board[r][c] = '.'
                rows[r] ^= pick
                cols[c] ^= pick
                boxes[box_index] ^= pick

                available ^= pick  # remove this digit from available

            # Put cell back
            empty.append((r, c))
            return False

        backtrack()