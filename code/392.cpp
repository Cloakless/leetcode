class Solution {
public:
    bool isSubsequence(string s, string t) {
        int t_index = 0;
        int t_len = t.size();
        int s_len = s.size();
        for (int i = 0; i < s_len; i++) {
            while (t_index < t_len && t[t_index] != s[i]) {
                t_index++;
            }
            if (t_index >= t_len) {
                    return false;
            }
            t_index++;
        }
        return true;
    }
};
