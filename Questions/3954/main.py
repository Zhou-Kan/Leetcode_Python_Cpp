def sum_of_good_integers(n: int, k: int) -> int:
    # according to the requirement, the range of x should be between n - k and n + k
    if k <= 0:
        return 0
    
    ans = 0
    # to loop through all numbers within that range to find out all compatible numbers
    for x in range(max(n - k, 0), n + k + 1):
        if n & x == 0:
            ans += x

    return ans

print(sum_of_good_integers(2, 3))
print(sum_of_good_integers(5, 1))
print(sum_of_good_integers(1, 15))
