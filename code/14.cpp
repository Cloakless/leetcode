class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(), strs.end());
        int n = strs[0].size();
        string best = "";
        bool all_same = true;
        for (int i = 0; i < n; i++) {
            char first = strs[0][i];
            for (int j = 0; j < strs.size(); j++) {
                if (strs[j][i] != first) {
                    all_same = false;
                }
            }
            if (!all_same) {
                return best;
            }
            else {
                best = strs[0].substr(0,i+1);
            }
        }
        return best;
        
    }
};
