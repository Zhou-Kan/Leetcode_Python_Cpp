def guess_number(n: int) -> int:
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2
        ret = guess(mid) 
        if ret > 0:
            left = mid + 1
        else:        
            right = mid 

    return left