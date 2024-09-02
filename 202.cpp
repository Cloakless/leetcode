class Solution {
public:
    bool isHappy(int n) {
        set<int> seen_set = {};
        while (true) {
            if (n == 1) {
                return true;
            }
            else {
                if (seen_set.count(n) == 1) {
                    return false;
                }
                seen_set.insert(n);
                int transform = 0;
                while (n > 0) {
                    int rem = n % 10;
                    transform += rem * rem;
                    n /= 10;
                }
                n = transform;
            }

        }
        
    }
};
