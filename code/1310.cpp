class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> ans (queries.size());
        // Calculate XOR of all elements to the left
        for (int i = 1; i < arr.size(); i++) {
            arr[i] = arr[i]^arr[i-1];
        }
        // Calculate queries
        for (int j = 0; j < queries.size(); j++) {
            if (queries[j][0] == 0) {
                ans[j] = arr[queries[j][1]];
            }
            else {
                ans[j] = arr[queries[j][1]]^arr[queries[j][0]-1];
            }
        }
        return ans;
    }
};
