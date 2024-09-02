class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int curr = 0;
        int min = 0;
        int best_index = 0;
        int n = cost.size();
        for (int i = 0; i < n; i++) {
            curr += gas[i];
            curr -= cost[i];
            if (curr < min) {
                best_index = (i + 1) % n;
                min = curr;
            }
        }
        if (curr < 0) {
            return -1;
        }
        return best_index;        
    }
};
