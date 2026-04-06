
public class Solution {
    public int maxSubArray(int[] nums) {
        // keep track of the minimum prefix and a running sum
        int minPreFix = 0, curSum = 0;
        int res = 0;

        for (int num : nums) {
            curSum += num;
            res = Math.max(res, curSum - minPreFix);
            minPreFix = Math.min(minPreFix, curSum);
        }

        return res;
    }
}

