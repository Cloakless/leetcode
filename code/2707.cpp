class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();
        vector<int> dp(n, 50);
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                dp[i] = dp[i-1] + 1;
            }
            else {
                dp[i] = 1;
            }
            for (int j = 0; j < dictionary.size(); j++) {
                string word = dictionary[j];
                int m = word.size();
                if (i == m - 1) {
                    if (s.substr(0,m) == word) {
                        dp[i] = 0;
                    }
                }
                else if (i >= m - 1) {
                        if (s.substr(i-m+1,m) == word) {
                            dp[i] = min(dp[i], dp[i-m]);
                    }

                }
            }
        }
        return dp[n-1];
    }
};
