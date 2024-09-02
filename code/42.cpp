class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int best_left[n];
        int left = 0;
        int right = 0;
        int best_right[n];
        for (int i = 0; i < n; i++) {
            if (height[i] > left) {
                left = height[i];
            }
            if (height[n-i-1] > right) {
                right = height[n-i-1];
            }
            best_left[i] = left;
            best_right[n-i-1] = right;
        }
        int tot = 0;
        int water = 0;
        for (int j = 0; j < n; j++) {
            water = min(best_left[j], best_right[j]);
            tot += water - height[j];
        }
        return tot;        
    }
};
