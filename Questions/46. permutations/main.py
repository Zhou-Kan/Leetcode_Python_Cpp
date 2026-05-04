def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans = []

    # using back track to get all possible results
    def back_track(path: list[int]) -> None:
        if len(path) == n:
            ans.append(path[:])
            return 

        for i in range(n):
            if path and path[-1] == nums[i]: continue 
            path.append(nums[i])
            print(path)
            back_track(path)
            path.pop()

    back_track([])
    return ans

print(permute([1, 2, 3]))