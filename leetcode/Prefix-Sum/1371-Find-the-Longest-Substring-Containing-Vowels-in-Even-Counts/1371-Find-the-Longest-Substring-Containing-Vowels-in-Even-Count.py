class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {0: -1}
        state = 0
        ans = 0
        vowels = 'aeiou'
        
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:
                state ^= 1 << j 
            if state not in idx:
                idx[state] = i
            ans = max(ans, i - idx[state])
        return ans
# TC: O(n)
# SC: O(32) 2^5 = 32