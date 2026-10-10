def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    
    # Initialize the answer array 
    ans = [1] * n

    # Calculate left products into the answer array
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    
    right_product = 1
    # Calculate right products into the answer array
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        ans[i] = ans[i] * right_product
    
    return ans

print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))

    