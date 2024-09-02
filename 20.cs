public class Solution {
    public bool IsValid(string s) {
        Stack<char> myStack = new Stack<char>();
        foreach (char c in s) {
            char d;
            switch (c) {
                case '(':
                    myStack.Push(c);
                    break;
                case ')':
                    if (myStack.Count == 0) {
                        return false;
                    }
                    d = myStack.Pop();
                    if (d != '(') {
                        return false;
                    }
                    break;
                case '[':
                    myStack.Push(c);
                    break;
                case ']':
                    if (myStack.Count == 0) {
                        return false;
                    }
                    d = myStack.Pop();
                    if (d != '[') {
                        return false;
                    }
                    break;
                case '{':
                    myStack.Push(c);
                    break;
                case '}':
                    if (myStack.Count == 0) {
                        return false;
                    }
                    d = myStack.Pop();
                    if (d != '{') {
                        return false;
                    }
                    break;
                default:
                    return false;
                    break;
            }
        }
        if (myStack.Count > 0) {
            return false;
        }
        return true;
    }
}
