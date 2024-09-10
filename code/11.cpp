class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int lower = 0;
        int upper = n - 1;
        int curr;
        int best = (upper - lower) * min(height[lower], height[upper]);
        while (upper > lower) {
            best = max(best, (upper - lower) * min(height[lower], height[upper]));
            if (height[lower] < height[upper]) {
                curr = height[lower];
                while (height[lower] <= curr && lower < upper) {
                    lower++;
                }
            }
            else {
                curr = height[upper];
                while (height[upper] <= curr && lower < upper) {
                    upper--;
                }
            }
        }
        return best;        
    }
};
