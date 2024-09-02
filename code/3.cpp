class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        if (n < 2) {
            return n;
        }
        unordered_map<char, int> counter;
        int best = 1;
        int left = 0;
        int right = 0;
        counter[s[0]] = 1;
        while (right < n - 1) {
            if (!counter.count(s[right+1]) || counter[s[right+1]] == 0) {
                right++;
                counter[s[right]] = 1;
                best = max(best, right - left + 1);
            }
            else {
                if (left == right) {
                    right++;
                }
                counter[s[left]] = 0;
                left++;
                counter[s[left]] = 1;
            }
        }
        return best;        
    }
};
