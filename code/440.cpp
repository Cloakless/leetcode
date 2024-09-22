class Solution {
public:
    int findKthNumber(int n, int k) {
        int prefix = 1;
        k--;
        while (k > 0) {
            // Count how many numbers there are with our current prefix
            // Either the answer is in our subtree or in one of our siblings'
            int num_children = countChildren(n, prefix, prefix+1);
            if (num_children <= k) {
                prefix++;
                k -= num_children;
            }
            else {
                k--;
                prefix *= 10;
            }
        }
        return prefix;
        
    }
private:
    int countChildren(int n, long start, long end) {
        int children = 0;
        while (start <= n) {
            children += min(end, (long)n+1) - start;
            start *= 10;
            end *= 10;
        }
        return children;
    }
};
