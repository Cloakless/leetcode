int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 1) {
        return 1;
    }
    int i = 0;
    int j = 0;
    int k = 1;
    while (j < numsSize - 1) {
        j++;
        if (nums[j] != nums[j-1]) {
            // We've found a new element
            i++;
            nums[i] = nums[j];
            k++;
        }
    }
    return k;
}
