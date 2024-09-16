class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        sort(timePoints.begin(), timePoints.end());
        int best = 24*60;
        int mins;
        int hours;
        hours = 10*(timePoints[0][0]-'0') + (timePoints[0][1]-'0') + 24;
        mins = 10*(timePoints[0][3]-'0') + (timePoints[0][4]-'0');
        string last = to_string(hours) + ":";
        if (mins < 10) {
            last = last + "0";
        }
        last = last + to_string(mins);
        timePoints.push_back(last);
        for (int i = 0; i < timePoints.size()-1; i++) {
            hours = 10*((timePoints[i+1][0])-(timePoints[i][0])) + ((timePoints[i+1][1])-(timePoints[i][1]));
            mins = 10*((timePoints[i+1][3])-(timePoints[i][3])) + ((timePoints[i+1][4])-(timePoints[i][4]));
            mins += 60*hours;
            best = min(best, mins);
        }
        return best;
    }
};
