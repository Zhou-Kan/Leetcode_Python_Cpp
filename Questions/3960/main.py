from collections import defaultdict

def get_length(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    ans = 0

    # i is the left side of the window
    for i in range(n):
        count = defaultdict(int) # the count of all elements
        cc = defaultdict(int) # the frequency of each occurrence
        # j is the right side of the window
        for j in range(i, n):
            x = nums[j]
            c = count[x] # previous count
            if c > 0:
                cc[c] -= 1
                if cc[c] == 0:
                    del cc[c]
            
            count[x] += 1
            cc[count[x]] += 1

            if len(count) == 1:
                ans = max(ans, j - i + 1)
            elif len(cc) == 2:
                c1, c2 = sorted(cc)
                if c1 * 2 == c2:
                    ans = max(ans, j - i + 1)
    
    return ans
            




print(get_length([1,2,2,1,2,3,3,3]))
print(get_length([5,5,5,5]))
print(get_length([1,2,3,4]))