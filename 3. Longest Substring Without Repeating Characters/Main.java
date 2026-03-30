import java.util.*;

public class Main {

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
    public static void main(String[] args) {
        Main test1 = new Main();
        System.out.println(test1.lengthOfLongestSubstring("abcabcbb"));
    }
}
