class Solution {
public:
    int mySqrt(int x) {
        long ans = 0;
        if (x == 0) {
            return ans;
        }
        ans++;
        if (x == 1) {
            return ans;
        }
        float mult = 2;
        while (ans*ans <= x) {
            if ((ans+1)*(ans+1) > x) {
                return ans;
            }
            else if (ans*ans*mult*mult < x) {
                ans *= mult;
            }
            else {
                mult = (mult + 1) / 2;
                ans += 1;
            }
        }
        return ans;
    }
};
