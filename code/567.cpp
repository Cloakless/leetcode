class Solution {
private:
    bool sameLetters(vector<int> a, vector<int>b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        return true;
    }

public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) {
            return false;
        }
        vector<int> c1(26, 0);
        vector<int> c2(26, 0);
        for (char c: s1) {
            c1[c-'a'] += 1;
        }

        for (int j = 0; j < s1.size(); j++) {
            c2[s2[j] - 'a'] += 1;
        }

        for (int k = s1.size(); k < s2.size() + 1; k++) {
            if (sameLetters(c1, c2)) {
                return true;
            }
            if (k == s2.size()) {
                return false;
            }
            c2[s2[k]-'a'] += 1;
            c2[s2[k-s1.size()]-'a'] -= 1;

        }
        return false;
    }
};
