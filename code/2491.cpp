class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        long long chemistry = 0;
        int sum = 0;
        int n = skill.size();
        unordered_map<int, int> counter;
        for (int i = 0; i < n; i++) {
            int num = skill[i];
            sum += num;
            if (counter.contains(num)) {
                counter[num] += 2;
            }
            else {
                counter[num] = 2;
            }
        }
        if ((2 * sum) % n != 0) {
            return -1;
        }
        int target = 2 * sum / n;
        for (int j = 0; j < n; j++) {
            int a = skill[j];
            int b = target - a;
            chemistry += a*b;
            if (counter[a] == 0) {
                return -1;
            }
            else {
                counter[a] -= 1;
            }
            if (counter[b] == 0) {
                return -1;
            }
            else {
                counter[b] -= 1;
            }
        }
        return chemistry / 2;
    }
};
