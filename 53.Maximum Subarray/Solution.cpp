#include<iostream>
using namespace std;

int maxSubArray(vector<int>& nums) {
    // curMin tracks the minimum prefix
    // curMax tracks a running sum
    int curSum = 0, curMin = 0;
    int ret = INT_MIN;
    
    for (int num : nums) {
        curSum += num;
        ret = max(ret, curSum - curMin);
        curMin = min(curMin, curSum);
    }
    return ret;
}