public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);
        Array.Reverse(happiness);
        long tot = 0;
        for (int i = 0; i < k; i++) {
            if (happiness[i] > i) {
                tot += (happiness[i] - i);
            }
            else {
                break;
            }
        }
        return tot;        
    }
}
