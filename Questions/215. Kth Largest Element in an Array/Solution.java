// Input: nums = [3,2,1,5,6,4], k = 2
// Output: 5

import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        int maxValue = Integer.MIN_VALUE, minValue = Integer.MAX_VALUE;
        for (int num : nums) {
            maxValue = Math.max(maxValue, num);
            minValue = Math.min(minValue, num);
        }
        int size = maxValue - minValue + 1;
        int[] bucket = new int[size];
        Arrays.fill(bucket, 0);

        for (int num : nums) {
            bucket[num - minValue]++;
        }

        for (int i = size - 1; i >= 0; i--) {
            k -= bucket[i];
            if (k <= 0) {
                return i + minValue;
            }
        }
        return -1;
    }

}
