# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

def convert(s: str, num_rows: int) -> str:
    # create a list to store each row of the result
    if num_rows <= 1:
        return s
    
    lst = [''] * num_rows

    n = len(s)
    row = 0
    d = 1

    for i in range(n):
        if i != 0 and i % (num_rows - 1) == 0:
            d *= -1

        lst[row] += s[i]
        row += d

    

    return ''.join(lst)

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 1))
print(convert("", 3))

