from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return True

        min_val = min(arr)
        max_val = max(arr)

        # If difference not divisible, cannot form AP
        if (max_val - min_val) % (n - 1) != 0:
            return False

        diff = (max_val - min_val) // (n - 1)
        if diff == 0:
            return len(set(arr)) == 1

        seen = set(arr)

        # Check every expected element exists
        for i in range(n):
            if min_val + i * diff not in seen:
                return False

        return True
    


"""
#include <stdlib.h>
#include <stdbool.h>

int compare(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    return (x > y) - (x < y);
}

bool canMakeArithmeticProgression(int* arr, int arrSize) {
    if (arrSize <= 2)
        return true;

    // Sort the array
    qsort(arr, arrSize, sizeof(int), compare);

    int diff = arr[1] - arr[0];

    for (int i = 2; i < arrSize; i++) {
        if (arr[i] - arr[i - 1] != diff)
            return false;
    }

    return true;
}


"""