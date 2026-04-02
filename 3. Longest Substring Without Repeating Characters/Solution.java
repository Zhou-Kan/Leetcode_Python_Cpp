import java.util.*;

public class Solution {

    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int left = 0, right = 0, n = s.length();
        int ret = 0;
        while (right < n) {
            char c = s.charAt(right);
            map.put(c, map.getOrDefault(c, 0) + 1);

            while (map.get(c) > 1) {
                char lc = s.charAt(left);
                map.put(lc, map.get(lc) - 1);
                
                left++;
            }
            ret = Math.max(right - left + 1, ret);
            right++;
        }
        
        return ret;
    }

}
