function maxSubArray(nums: number[]): number{
    let curSum = 0, curMin = 0
    let res = -Infinity

    for (const num of nums) {
        curSum += num
        res = Math.max(res, curSum - curMin)
        curMin = Math.min(curMin, curSum)
    }
    return res
}