
public class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        char[] charArray = s.toCharArray();
        int start = 0, end = 0;

        for (int i = 0; i < 2 * n - 1; i++) {
            int left = i / 2;
            int right = (i + 1) / 2;
            while (left >= 0 && right < n && charArray[left] == charArray[right]) {
                left--;
                right++;
            }
            if (right - left > end - start) {
                start = left;
                end = right;
            }
        }
        return s.substring(start + 1, end);
    }
    
}
