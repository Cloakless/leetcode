class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int m_tot = std::accumulate(rolls.begin(), rolls.end(), 0);
        int tot = (m+n) * mean;
        int n_tot = tot - m_tot;
        if (n_tot < n || n_tot > 6*n) {
            vector<int> answer = {};
            return answer;
        }
        vector<int> answer(n, 1);
        int i = 0;
        n_tot -= n; // Take off the 1s which are already there
        while (n_tot > 0) {
            int next_roll = min(5, n_tot);
            answer[i] += next_roll;
            n_tot -= next_roll;
            i++;
        }
        return answer;
    }
};
