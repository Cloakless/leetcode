class Solution {
public:
    bool allDifferent(vector<char> numbers) {
        sort(numbers.begin(), numbers.end());
        int i = 0;
        while (numbers[i] == '.' && i < 8) {
            i++;
        }
        for (int j = i; j < 8; j++) {
            if (numbers[j] == numbers[j+1]) {
                for (int x = 0; x < 9; x++) {
                }
                return false;
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        // test rows
        for (int row = 0; row < 9; row++) {
            if (!allDifferent(board[row])) {
                return false;
            }
        }
        // test cols
        for (int col = 0; col < 9; col++) {
            vector<char> column = {board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col], board[6][col], board[7][col], board[8][col]};
            if (!allDifferent(column)) {
                return false;
            }
        }
        // test squares
        for (int x_offset = 0; x_offset < 9; x_offset += 3) {
            for (int y_offset = 0; y_offset < 9; y_offset += 3) {
                vector<char> square = {board[x_offset][y_offset], board[x_offset][y_offset+1], board[x_offset][y_offset+2], board[x_offset+1][y_offset], board[x_offset+1][y_offset+1], board[x_offset+1][y_offset+2], board[x_offset+2][y_offset], board[x_offset+2][y_offset+1], board[x_offset+2][y_offset+2]};
                if (!allDifferent(square)) {
                    return false;
                }
            }         
        }
        return true;        
    }
};
