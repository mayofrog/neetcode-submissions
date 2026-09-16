class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i, j = 0, 1
        chars = {s[0]}
        count = 1

        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                count = max(count, j - i + 1)

            else:
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1

                chars.remove(s[i])
                i += 1
                chars.add(s[j])

            j += 1

        return count