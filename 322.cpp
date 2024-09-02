class Solution {
public:
    int memo [10001];
    int dp(vector<int>& coins, int amount) {
        int min;
        if (this->memo[amount] != -2) {
            return this->memo[amount];
        }
        int numCoins = coins.size();
        if (amount % coins[numCoins-1] == 0) {
            min = amount / coins[numCoins-1];
        }
        else {
            min = -1;
            for (int i = 0; i < numCoins; i++) {
                if (amount - coins[i] >= 0) {
                    int cand = dp(coins, amount - coins[i]);
                    if (cand != -1) {
                        if (cand + 1 < min || min == -1) {
                            min = cand + 1;
                        }
                    }
                }
            }
        }
        memo[amount] =  min;
        return min;
    }
    int coinChange(vector<int>& coins, int amount) {
        for (int j = 0; j <= 10000; j++) {
            memo[j] = -2;
        }
        memo[0] = 0;
        for (int k = 0; k < coins.size(); k++) {
            if (coins[k] <= 10000) {
                memo[coins[k]] = 1;
            }
        }
        sort(coins.begin(), coins.end());
        int ans = dp(coins, amount);
        return ans;        
    }
};
