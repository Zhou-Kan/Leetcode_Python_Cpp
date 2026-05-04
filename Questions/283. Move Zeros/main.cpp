#include<iostream>
using namespace std;

class Solution{
    public:
        void moveZeroes(vector<int>& nums) {
            int n = nums.size();
            int read = 0, write = 0;
            while (read < n) {
                if (nums[read] != 0) {
                    swap(nums[read], nums[write++]);
                }
                read++;
            }
        }
};