class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        // We'll store zeros in the first row/col so check whether they have one originally
        bool wipe_first_row = false;
        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == 0) {
                wipe_first_row = true;
                break;
            }
        }
        bool wipe_first_col = false;
        for (int j = 0; j < m; j++) {
            if (matrix[j][0] == 0) {
                wipe_first_col = true;
                break;
            }
        }
        // Record which rows / cols have zeros
        for (int a = 1; a < m; a++) {
            for (int b = 1; b < n; b++) {
                if (matrix[a][b] == 0) {
                    matrix[a][0] = 0;
                    matrix[0][b] = 0;
                }
            }
        }
        // Now wipe
        for (int a = 1; a < m; a++) {
            for (int b = 1; b < n; b++) {
                if (matrix[a][0] == 0 || matrix[0][b] == 0) {
                    matrix[a][b] = 0;
                }
            }
        }
        // Fix up first row/col
        if (wipe_first_col) {
            for (int x = 0; x < m; x++) {
                matrix[x][0] = 0;
            }
        }
        if (wipe_first_row) {
            for (int y = 0; y < n; y++) {
                matrix[0][y] = 0;
            }
        } 
    }
};
