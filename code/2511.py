class Solution {
public:
    int captureForts(vector<int>& forts) {
        int streak = 0;
        int best = 0;
        bool minus_start = false;
        bool plus_start = false;
        for (int i = 0; i < forts.size(); i++) {
            switch (forts[i]) {
                case 0:
                    streak++;
                    break;
                case 1:
                    if (minus_start) {
                        best = max(best, streak);
                    }
                    streak = 0;
                    minus_start = false;
                    plus_start = true;
                    break;
                case -1:
                    if (plus_start) {
                        best = max(best, streak);
                    }
                    streak = 0;
                    minus_start = true;
                    plus_start = false;
                    break;
            }
        }
        return best;   
    }
};
