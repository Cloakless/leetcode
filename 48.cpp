class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int t1;
        int t2;
        // All rotations are two reflections
        // First flip along long diagonal
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < a; b++) {
                t1 = matrix[a][b];
                t2 = matrix[b][a];
                matrix[a][b] = t2;
                matrix[b][a] = t1;
            }
        }
        // Then flip along the y-axis
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n/2; j++) {
                t1 = matrix[i][j];
                t2 = matrix[i][n-j-1];
                matrix[i][n-j-1] = t1;
                matrix[i][j] = t2;
            }
        }        
    }
};
