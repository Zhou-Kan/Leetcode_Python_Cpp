function lengthOfLongestSubstring(s) {
    const map = new Map()
    let left = 0, right = 0
    const n = s.length
    let ret = 0

    while (right < n) {
        const c = s[right]
        map.set(c, (map.get(c) || 0) + 1)
        
        while (left < right && map.get(c) > 1) {
            const lc = s[left]
            map.set(lc, map.get(lc) - 1)
            left++
        }
        ret = Math.max(ret, right - left + 1)
        right++
    }
    return ret
}

console.log(lengthOfLongestSubstring("abcabcbb"));
