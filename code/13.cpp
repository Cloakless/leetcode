class Solution {
public:
    int romanToInt(string s) {
        int n = s.size();
        int c = 0;
        int ans = 0;
        while (c < n) {
            switch (s[c]) {
                case 'M':
                    ans += 1000;
                    break;
                case 'D':
                    ans += 500;
                    break;
                case 'C':
                    if (c < n - 1 && s[c+1] == 'M') {
                        ans += 900;
                        c++;
                    }
                    else if (c < n - 1 && s[c+1] == 'D') {
                        ans += 400;
                        c++;
                    }
                    else {
                        ans += 100;
                    }
                    break;
                case 'L':
                    ans += 50;
                    break;
                case 'X':
                    if (c < n - 1 && s[c+1] == 'L') {
                        ans += 40;
                        c++;
                    }
                    else if (c < n - 1 && s[c+1] == 'C') {
                        ans += 90;
                        c++;
                    }
                    else {
                        ans += 10;
                    }
                    break;
                case 'V':
                    ans += 5;
                    break;
                case 'I':
                    if (c < n - 1 && s[c+1] == 'X') {
                        ans += 9;
                        c++;
                    }
                    else if (c < n - 1 && s[c+1] == 'V') {
                        ans += 4;
                        c++;
                    }
                    else {
                        ans += 1;
                    }
                    break;
            }
            c++;
        }
        return ans;      
    }
};
