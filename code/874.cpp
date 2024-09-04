class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        set<int> blocks;
        // Hash of obstacle = 30001X + Y
        int hash_scale = 60001;
        for (int i = 0; i < obstacles.size(); i++) {
            blocks.insert(obstacles[i][0]*hash_scale + obstacles[i][1]);
        }

        int curr_x = 0;
        int curr_y = 0;
        int x = 0;
        int y = 0;
        int direction = 0; // North
        int best = 0;
        for (int j = 0; j < commands.size(); j++) {
            // Process instructions
            if (commands[j] == -2) {
                direction += 3;
                direction = direction % 4;
            }
            else if (commands[j] == -1) {
                direction += 1;
                direction = direction % 4;
            }
            else {
                // Get ready to advance
                switch(direction) {
                    case 0:
                        // Pointing north, so steps don't affect X but do affect Y
                        x = 0;
                        y = 1;
                        break;
                    case 1:
                        // East
                        x = 1;
                        y = 0;
                        break;
                    case 2:
                        // South
                        x = 0;
                        y = -1;
                        break;
                    case 3:
                        // West
                        x = -1;
                        y = 0;
                        break;
                    default:
                        // ??
                }
                for (int step = 0; step < commands[j]; step++) {
                    int new_x = curr_x + x;
                    int new_y = curr_y + y;
                    if (blocks.count(hash_scale*new_x + new_y) == 1) {
                        break;
                    }
                    else {
                        curr_x = new_x;
                        curr_y = new_y;
                        if (curr_x*curr_x + curr_y*curr_y > best) {
                            best = curr_x*curr_x + curr_y*curr_y;
                        }
                    }
                }
            }
        }
        return best;        
    }
};
