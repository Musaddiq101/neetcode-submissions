class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        n = len(s)
        maxLen = 0
        seen = set()
        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            maxLen = max(maxLen, r-l+1)
            seen.add(s[r])
            r += 1

        return maxLen
                

        