class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int carry = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (carry != 0) {
                if (digits[i] == 9) {
                    digits[i] = 0;
                }
                else {
                    digits[i] += 1;
                    carry = 0;
                }
            }
            else {
                break;
            }
        }
        if (carry != 0) {
            // The number was all 9s
            digits.resize(n+1);
            digits[n] = 0;
            digits[0] = 1;
        }
        return digits;        
    }
};
