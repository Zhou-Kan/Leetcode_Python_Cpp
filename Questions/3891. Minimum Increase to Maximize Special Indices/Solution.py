def min_increase(nums: list[int]) -> int:
    n = len(nums)
    k = n // 2 if n % 2 != 0 else (n - 1) % 2 

    dp = [[float('inf') for _ in range(k + 1)] for _ in range(n)]

    for i in range(1, n - 1):
        print(i)
        for j in range(k):
            #print(i)
            if i == 1:
                if nums[i - 1] < nums[i] < nums[i + 1]:
                    dp[i][1] = 0
                else:
                    cost = max(nums[i + 1], nums[i - 1]) - nums[i] + 1
                    dp[i][1] = cost
                #print(i)
            else:
                #print(i)
                if nums[i - 1] < nums[i] < nums[i + 1]:
                    
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 1]) if dp[i - 2][j - 1] != inf else 0
                else:
                    cost = max(nums[i + 1], nums[i - 1]) - nums[i] + 1 
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 1] + cost) if dp[i - 2][j - 1] != inf else cost

        #print(dp)
        ret = min(dp[i][k] for i in range(1, n - 1))
        return -1
    
print(min_increase([5, 2, 1, 4, 3]))