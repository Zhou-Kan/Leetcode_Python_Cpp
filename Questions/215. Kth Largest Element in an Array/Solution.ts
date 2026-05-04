function findKthLargest(nums: number[], k: number): number {
    const minValue = nums.reduce((a, b) => Math.min(a, b), Infinity)
    const maxValue = nums.reduce((a, b) => Math.max(a, b), -Infinity)
    const size = maxValue - minValue + 1
    const bucket: number[] = Array(size).fill(0)

    for (const num of nums) {
        bucket[num - minValue]++
    }

    for (let i = size - 1; i >= 0; i--) {
        k -= bucket[i]
        if (k <= 0) return i + minValue
    }
    return -1
}

const ret = findKthLargest([3,2,1,5,6,4], 2)
console.log(ret);
