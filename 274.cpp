class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n = citations.size();
        for (int i = 0; i < n; i++) {
            if (citations[n - i - 1] < i + 1) {
                return i;
            }
        }
        return n;        
    }
};
