
def find_duplicate(nums: list[int]) -> int:
    # 【1, 3, 4, 2, 2] output 2
    #  
    n = len(nums)

    for i, num in enumerate(nums):
        idx = num % n
        if nums[idx - 1] > n:
            return idx
        nums[idx - 1] += n

    return n + 1
