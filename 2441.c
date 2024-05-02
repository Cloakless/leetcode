int findMaxK(int* nums, int numsSize) {
    int best = -1;
    for (int i=0; i < numsSize; i++) {
        for (int j=i+1; j < numsSize; j++) {
            if (nums[j] == -1*nums[i]) {
                if (nums[j] > nums[i]) {
                    if (nums[j] > best) {
                        best = nums[j];
                    }
                }
                else {
                    if (nums[i] > best) {
                        best = nums[i];
                    }
                }
            }
        }
    }
    return best;
}
