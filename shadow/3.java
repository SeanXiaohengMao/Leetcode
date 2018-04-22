class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0;
        int res = 0;
        int n = s.length();
        Set<Character> set = new HashSet<>();

        while (i < n && j < n) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j));
                j++;
                res = Math.max(res, j - i);
            }
            else {
                set.remove(s.charAt(i));
                i++;
            }
        }
        return res;
    }
}
