def generate_parenthesis(n: int) -> list[str]:
    ans = []

    def backtrack(left: int, right: int, path: str) -> None:
        if left == right == n:
            ans.append(path[:])

        if left < n:
            backtrack(left + 1, right, path + '(')

        if left > right:
            backtrack(left, right + 1, path + ')')

    backtrack(0, 0, '')
    return ans

print(generate_parenthesis(3))
print(generate_parenthesis(0))

