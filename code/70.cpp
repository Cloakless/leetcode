class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }

        int paths[n+1];
        paths[0] = 1;
        paths[1] = 1;
        paths[2] = 2;
        for (int i = 3; i <= n; i++) {
            paths[i] = paths[i-1] + paths[i-2];
        }
        return paths[n];        
    }
};
