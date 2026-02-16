from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use bitmasking for rows, columns, and boxes.
        
        rows[i] stores seen digits in row i
        cols[j] stores seen digits in column j
        boxes[k] stores seen digits in 3x3 box k
        
        Each digit maps to a bit position (0–8).
        
        If bit already set → duplicate found → return False.
        
        Time Complexity: O(81) = O(1)
        Space Complexity: O(1)
        """
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = int(board[r][c]) - 1
                mask = 1 << num
                
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check duplicate
                if (rows[r] & mask) or (cols[c] & mask) or (boxes[box_index] & mask):
                    return False
                
                # Set bit
                rows[r] |= mask
                cols[c] |= mask
                boxes[box_index] |= mask
        
        return True
