class Solution {
public:
    int minBitFlips(int start, int goal) {
        int ans = 0;
        int checker = 1;
        while (checker <= max(start, goal)) {
            if (((start^goal) & checker) == checker) {
                ans += 1;
            }
            checker *= 2;
        }
        return ans;
    }
};
