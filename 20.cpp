class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        int n = s.size();
        char c;
        for (int i = 0; i < n; i++) {
            c = s[i];
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            else {
                if (stack.empty()) {
                    return false;
                }
                if (c == ')') {
                    if (stack.top() != '(') {
                        return false;
                    }
                }
                if (c == '}') {
                    if (stack.top() != '{') {
                        return false;
                    }
                }
                if (c == ']') {
                    if (stack.top() != '[') {
                        return false;
                    }
                }
                stack.pop();
            }
        }
        // We shouldn't have any unclosed brackets
        return stack.empty();
    }
};
