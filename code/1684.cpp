class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int ans = 0;
        set<char> valid;
        for (int i = 0; i < allowed.size(); i++){
            valid.insert(allowed[i]);
        }
        for (int j = 0; j < words.size(); j++) {
            string word = words[j];
            bool is_good = true;
            for (int k = 0; k < word.size(); k++) {
                if (!valid.contains(word[k])) {
                    is_good = false;
                }
            }
            if (is_good) {
                ans++;
            }
        }
        return ans;
    }
};
