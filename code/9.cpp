class Solution {
public:
    bool isPalindrome(int x) {
        long original = x;
        long new_num = 0;
        while (x > 0) {
            new_num *= 10;
            new_num += x % 10;
            x /= 10;
        }
        if (original == new_num) {
            return true;
        }
        return false;
    }
};
