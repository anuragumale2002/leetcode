class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses bits of a 32-bit unsigned integer.
        
        Explanation:
        -----------
        We process exactly 32 bits.
        
        At each step:
        1. Extract last bit of n using (n & 1)
        2. Shift result left to make space
        3. Add extracted bit to result
        4. Right shift n
        
        Why 32 iterations?
        Because problem guarantees 32-bit input.
        
        Time Complexity: O(1)  (32 iterations = constant)
        Space Complexity: O(1)
        """
        
        result = 0
        
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
            
        return result
