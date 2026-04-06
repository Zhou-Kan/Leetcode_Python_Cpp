function longestPalindrome(s: string): string{
    const n = s.length
    let start = 0, end = 0

    for(let i = 0; i < 2 * n - 1; i++) {
        let left = Math.floor(i / 2), right = Math.floor((i + 1) / 2)
        while (left >= 0 && right < n && s[left] === s[right]) {
            left--
            right++
        }
        if (right - left > end - start) {
            end = right
            start = left
        }
    }
    return s.substring(start + 1, end)
}