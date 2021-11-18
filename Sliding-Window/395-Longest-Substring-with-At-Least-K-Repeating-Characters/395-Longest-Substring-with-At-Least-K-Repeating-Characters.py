class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        
        for unique_characters in range(1, len(set(s)) + 1):
            freq = [0] * 26
            left, right = 0, 0
            cnt_diffs, cnt_k = 0, 0
            
            while right < len(s):
                if cnt_diffs <= unique_characters:
                    right_idx = ord(s[right]) - ord('a')
                    freq[right_idx] += 1
                    right += 1

                    if freq[right_idx] == 1:
                        cnt_diffs += 1
                    if freq[right_idx] == k:
                        cnt_k += 1
                else:
                    left_idx = ord(s[left]) - ord('a')
                    if freq[left_idx] == 1:
                        cnt_diffs -= 1
                    if freq[left_idx] == k:
                        cnt_k -= 1
                    freq[left_idx] -= 1
                    left += 1
            
                if cnt_k == cnt_diffs == unique_characters:
                    res = max(res, right - left)
        
        return res