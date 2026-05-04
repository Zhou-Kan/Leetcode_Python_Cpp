def majority_element(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    candidate = nums[0]
    times = 1

    # to check whether the candidate appears more than n/2 times
    for num in nums[1:]:
        if num != candidate:
            times -= 1
            if times == 0:
                candidate = num
                times = 1
        else:
            times += 1
    
    return candidate

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))