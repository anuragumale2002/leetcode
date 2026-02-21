class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        root = int(total ** 0.5)
        
        return root if root * root == total else -1


"""
#include <math.h>

int pivotInteger(int n) {
    long long total = (long long)n * (n + 1) / 2;
    
    long long root = (long long)sqrt(total);
    
    if (root * root == total)
        return (int)root;
    
    return -1;
}


"""