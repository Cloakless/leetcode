class Solution {
public:
    bool isLetter(char c) {
        int val = int(c);
        if (((65 <= val) && (val <= 90)) ||  (97 <= val) && (val <= 122) || (48 <= val) && (val <= 57)) {
            return true;
        }
        return false;
    }
    bool isPalindrome(string s) {
        int front = 0;
        int n = s.size();
        int back = n - 1;
        while (!isLetter(s[front])) {
            if (front == n) {
                // String has no letters
                return true;
            }
            front++;
        }
        while (!isLetter(s[back])) {
            back--;
        }
        while (front < n) {
            int f_val = int(s[front]);
            if (f_val >= 97) {
                f_val -= 32;
            }
            int b_val = int(s[back]);
            if (b_val >= 97) {
                b_val -= 32;
            }
            if (f_val != b_val) {
                return false;
            }
            front++;
            back--;
            while (front < n && !isLetter(s[front])) {
                front++;
            }
            while (back > 0 && !isLetter(s[back])) {
                back--;
            }
        }
        return true;
    }
};
