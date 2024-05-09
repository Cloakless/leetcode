public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            for (int j = 0; j < n; j++) {
                nums1[j] = nums2[j];
            }
            return;
        }
        int i = m + n;
        m--;
        n--;
        i--;
        while (i >= 0) {
            Console.WriteLine(i);
            Console.WriteLine(m);
            Console.WriteLine(n);

            if (m >= 0 && (n < 0 || nums1[m] > nums2[n])) {
                nums1[i] = nums1[m];
                m--;
            }
            else {
                nums1[i] = nums2[n];
                n--;
            }
            i--;
        }
    }
}
