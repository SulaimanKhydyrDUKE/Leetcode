
##Longest Substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        map = {}
        l = 0
        maks = 0

        for r in range(len(s)):

            while s[r] in maps:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1

            map[s[r]] = 1
            maks = max(maks, r - l + 1)

        return maks
