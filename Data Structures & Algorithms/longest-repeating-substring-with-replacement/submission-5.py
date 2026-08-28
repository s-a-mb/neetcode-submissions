class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        chars = {}
        size = l = max_freq = 0

        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            max_freq = max(max_freq, chars[s[r]])

            while (r - l + 1) - max_freq > k:
                chars[s[l]] -= 1
                l += 1
            size = max(size, r - l + 1)

        return size