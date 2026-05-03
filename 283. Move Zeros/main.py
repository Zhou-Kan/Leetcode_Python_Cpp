def move_zeros(nums: list[int]) -> None:
    n = len(nums)
    read = write = 0
    while read < n:
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
        read += 1