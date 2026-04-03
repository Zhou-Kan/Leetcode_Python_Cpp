function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b)
    const ans: number[][] = []
    const n = nums.length

    for (let i = 0; i < n; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue
        let left = i + 1, right = n - 1
        while (left < right) {
            let total = nums[i] + nums[left] + nums[right]
            if (total === 0) {
                ans.push([nums[i], nums[left], nums[right]])
                left++
                right--
                while (left < right && nums[left] === nums[left - 1]) left++
                while (left < right && nums[right] === nums[right + 1]) right--
            } else if (total > 0) right--
            else left++
        }
    }
    return ans
}