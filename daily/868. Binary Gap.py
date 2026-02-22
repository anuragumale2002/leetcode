class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Finds the maximum distance between two consecutive 1's 
        in the binary representation of integer n.

        ----------------------------------------------------------
        WHY THIS APPROACH?
        ----------------------------------------------------------
        Instead of converting the number into a binary string,
        we directly work with bits using bit manipulation.

        Bit manipulation is:
        - More memory efficient (O(1) space)
        - Faster since no string conversion is required
        - Ideal when dealing with binary problems

        ----------------------------------------------------------
        HOW IT WORKS?
        ----------------------------------------------------------
        1. We iterate through each bit of the number using right shift.
        2. If current bit is 1:
            - If we have seen a previous 1,
              compute the distance.
            - Update the maximum distance.
        3. Keep track of the index of last seen 1.
        4. Continue until n becomes 0.

        ----------------------------------------------------------
        EXAMPLE:
        n = 22
        Binary = 10110

        Index:  0 1 2 3 4
                1 0 1 1 0

        Distances:
        2 - 0 = 2
        3 - 2 = 1

        Answer = 2
        ----------------------------------------------------------

        Time Complexity  : O(log n)
        Space Complexity : O(1)
        """

        last_position = -1   # Stores index of last seen '1'
        max_distance = 0     # Stores maximum gap
        current_index = 0    # Tracks current bit index

        while n > 0:
            # Check if the least significant bit is 1
            if n & 1:
                # If this is not the first 1
                if last_position != -1:
                    max_distance = max(max_distance, current_index - last_position)
                
                # Update last seen position
                last_position = current_index
            
            # Move to next bit
            n >>= 1
            current_index += 1

        return max_distance



"""
#include <stdio.h>

/*
    Function: binaryGap

    Purpose:
    Finds the maximum distance between consecutive 1's
    in the binary representation of a positive integer.

    Why bit manipulation?
    - Avoids extra memory usage (no binary string)
    - Faster execution
    - Direct hardware-level operations

    Time Complexity  : O(log n)
    Space Complexity : O(1)
*/

int binaryGap(int n) {
    int last_position = -1;  // Index of previous '1'
    int max_distance = 0;    // Maximum gap
    int current_index = 0;   // Current bit index

    while (n > 0) {
        // Check if current bit is 1
        if (n & 1) {
            if (last_position != -1) {
                int distance = current_index - last_position;
                if (distance > max_distance) {
                    max_distance = distance;
                }
            }
            last_position = current_index;
        }

        // Right shift to check next bit
        n = n >> 1;
        current_index++;
    }

    return max_distance;
}

/* Example usage */
int main() {
    int n = 22;
    printf("Binary Gap: %d\n", binaryGap(n));
    return 0;
}
"""