class Solution {
public:
    double myPow(double x, int n) {
        // Special cases, of varying pointlessness
        if (x == 1) {
            return 1;
        }
        if (x == -1) {
            return -1 + 2 * (n % 2 == 0);
        }
        if (n == -2147483648) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return x;
        }
        if (n < 0) {
            return 1 / myPow(x, -1 * n);
        }
        double part = myPow(x, n / 2);
        if (n % 2 == 0) {
            return part * part;
        }
        else {
            return part * part * x;
        }
    }
};
