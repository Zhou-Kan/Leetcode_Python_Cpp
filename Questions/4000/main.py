def largeest_integer(n: int, s: int) -> int:
    # Check if the largest possible number is less than s. It's impossible
    if n * 9 < s or s < 0:
        return -1

    ans = []
    # To pick the possible digit(up to 9) from left to right
    for _ in range(n):
        digit = min(9, s)
        ans.append(str(digit))
        s -= digit

    return int(''.join(ans))


print(largeest_integer(2, 9))
print(largeest_integer(9, 0))
print(largeest_integer(2, -1))
print(largeest_integer(2, 19))