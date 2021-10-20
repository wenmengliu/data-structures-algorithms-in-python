class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        start = 0
        ans = 0
        
        for end, ch in enumerate(s):
            if last[ord(ch)] != -1:
                # move starting pointer
                start = max(start, last[ord(ch)] + 1)
            ans = max(ans, end - start + 1)
            # save character index to update last arr
            last[ord(ch)] = end
        
        return ans