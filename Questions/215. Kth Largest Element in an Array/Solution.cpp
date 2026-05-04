#include<iostream>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    auto [min_it, max_it] = minmax_element(nums.begin(), nums.end());
    int minVal = *min_it, maxVal = *max_it;
    int size = maxVal - minVal + 1;
    vector<int> bucket(size, 0);

    for (int num : nums) {
        bucket[num - minVal]++;
    }

    for (int i = size - 1; i >= 0; i--) {
        k -= bucket[i];
        if (k <= 0) return i + minVal;
    }
    return 0;

}

int main() {
    vector<int> nums = {2, 1, 5, 6, 4};
    int ret = findKthLargest(nums, 2);
    cout << ret << endl;
    return 0;
}