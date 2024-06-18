public class Solution {
    public bool IsAnagram(string s, string t) {
        char[] schars = s.ToArray();
        Array.Sort(schars);
        char[] tchars = t.ToArray();
        Array.Sort(tchars);
        int n = schars.Length;
        int m = tchars.Length;
        if (n != m) {
            return false;
        }
        for (int i = 0; i < n; i++) {
            if (schars[i] != tchars[i]) {
                return false;
            }
        }
        return true;
    }
}
