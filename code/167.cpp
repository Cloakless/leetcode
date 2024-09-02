class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int first = 0;
        int second = 1;
        vector<int> ans = {0,0};
        int cand;
        while (true) {
            cand = numbers[first] + numbers[second];
            if (cand == target) {
                ans[0] = first + 1;
                ans[1] = second + 1;
                return ans;
            }
            if (cand < target && second < n - 1) {
                second++;
            }
            else {
                // cand > target or we can't exceed target starting so far left
                first++;
                while (numbers[first] + numbers[second] > target) {
                    second--;
                }
            }

        }
        return ans;
    }
};
