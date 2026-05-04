#include<iostream>
using namespace std;

vector<int> searchRange(vector<int>& nums, int target) {
    int n = nums.size();
    if (nums.empty()) return {-1, -1};
    int left = 0, right = n - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    if (nums[left] != target) return {-1, -1};

    int leftSize = left;
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        if (nums[mid] > target) {
            right = mid - 1;
        } else {
            left = mid;
        }
    }
    return {leftSize, left};
}