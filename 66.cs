public class Solution {
    public int[] PlusOne(int[] digits) {
        int n = digits.Length;
        for (int i = n - 1; i >= 0; i--)  {
            if (digits[i] != 9) {
                digits[i] += 1;
                break;
            }
            else {
                digits[i] = 0;
            }
        }
        if (digits[0] == 0) {
            int[] new_num = new int[n + 1];
            new_num[0] = 1;
            for (int j = 1; j <= n; j++) {
                new_num[j] = 0;
            }
            return new_num;
        }
        return digits;      
    }
}
