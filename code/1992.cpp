class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        int m = land.size();
        int n = land[0].size();
        vector<vector<int>> ans;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1) {
                    int x1 = i;
                    int y1 = j;
                    int x2 = i;
                    int y2 = j;
                    while (x2 < (m - 1) && land[x2+1][y1] == 1) {
                        x2++;
                    }
                    while (y2 < (n - 1) && land[x1][y2+1] == 1) {
                        y2++;
                    }
                    vector<int> cand = {x1, y1, x2, y2};
                    ans.push_back(cand);
                    for (int a = x1; a <= x2; a++) {
                        for (int b = y1; b <= y2; b++) {
                            land[a][b] = 0;
                        }
                    }
                }
            }
        }
        return ans;
        
    }
};
