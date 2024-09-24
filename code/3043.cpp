class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<string> prefixes;
        int best = 0;
        // Add all arr1 prefixes to the set
        for (int i = 0; i < arr1.size(); i++) {
            string word = to_string(arr1[i]);
            int len = word.size();
            for (int j = 0; j < len; j++) {
                prefixes.insert(word.substr(0,j+1));
            }
        }
        // Compare all arr2 prefixes
        for (int k = 0; k < arr2.size(); k++) {
            string word = to_string(arr2[k]);
            int len = word.size();
            for (int a = 0; a < len; a++) {
                if (prefixes.contains(word.substr(0,a+1))) {
                    best = max(best, a+1);
                }
            }
        }
        return best;
    }
};
