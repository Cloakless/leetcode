class Solution {
public:
    int trailingZeroes(int n) {
        int num_2s = 0;
        int num_5s = 0;
        int two_div = 2;
        int fiv_div = 5;
        // Calculate how many 2s and 5s there are in n!
        while (two_div <= n) {
            num_2s += n / two_div;
            two_div *= 2;
        }
        while (fiv_div <= n) {
            num_5s += n / fiv_div;
            fiv_div *= 5;
        }
        return min(num_2s, num_5s);        
    }
};
