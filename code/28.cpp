class Solution {
public:
    int strStr(string haystack, string needle) {
        int h = haystack.size();
        int n = needle.size();
        int ans = -1;
        for (int i = 0; i < h - n + 1; i++) {
            bool found = true;
            for (int j = 0; j < n; j++) {
                if (haystack[i+j] !=  needle[j]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                ans = i;
                break;
            }
        }
        return ans;
    }
};
