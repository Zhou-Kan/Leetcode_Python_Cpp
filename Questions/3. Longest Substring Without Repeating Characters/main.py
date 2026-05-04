from collections import defaultdict
def length_of_longest_substring(s: str) -> str:
    count = defaultdict(int)
    left = right = 0
    ret = 0

    while right < len(s):
        count[s[right]] += 1
        while left < right and count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1
        
        ret = max(ret, right - left + 1)
        right += 1

    return ret

assert length_of_longest_substring("abcabcbb") == 3
print(length_of_longest_substring("abcabcbb"))