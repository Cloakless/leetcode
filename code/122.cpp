class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int n = prices.size();
        if (n == 1) {
            return 0;
        }
        int curr_price = prices[0];
        for (int i = 1; i < n; i ++) {
            if (prices[i] > curr_price) {
                profit += prices[i] - curr_price;
            }
            curr_price = prices[i];
        }
    return profit;       
    }
};
