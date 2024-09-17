class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        // Map all elements to a list of where they appear
        unordered_map<int, vector<int>> indices;
        set<vector<int>> seen;
        for (int x = 0; x < nums.size(); x++) {
            int val = nums[x];
            if (!indices.contains(val)) {
                indices[val] = {x};
            }
            else {
                indices[val].push_back(x);
            }
        }
        int a;
        int b;
        int c;
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size(); i++) {
            a = nums[i];
            if (i == 0 || (i > 0 && a != nums[i-1])) {
                for (int j = i+1; j < nums.size(); j++) {
                    b = nums[j];
                    c = -1*(a + b);
                    if (indices.contains(c) && j < *std::max_element(indices[c].begin(),indices[c].end())) {
                        vector<int> triple = {a,b,c};
                        if (!seen.contains(triple)) {
                            seen.insert(triple);
                            ans.push_back(triple);
                        }
                    }
                }
            }
        }
        return ans;
    }
};
