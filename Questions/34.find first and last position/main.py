def search_range(nums: list[int], k: int) -> list[int]:
    n = len(nums)

    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < k:
            left = mid + 1
        else:
            right = mid
    
    if nums[left] != k:
        return [-1, -1]
    left_side = left
    left, right = 0, n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] > k:
            right = mid - 1
        else:
            left = mid 

    return [left_side, left]