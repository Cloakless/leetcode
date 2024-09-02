class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<int> future (prices.begin(), prices.begin() + n);
        int best = prices[n - 1];
        for (int i = n - 1; i >= 0; i--) {
            if (prices[i] > best) {
                best = prices[i];
            }
            future[i] = best;
        }
        int profit = 0;
        for (int j = 0; j < n; j++) {
            int potential = future[j] - prices[j];
            if (potential > profit) {
                profit = potential;
            }
        }
        return profit;
    }
};
