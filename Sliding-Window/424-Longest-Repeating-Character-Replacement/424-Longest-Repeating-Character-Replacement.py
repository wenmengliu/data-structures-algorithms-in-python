class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        window_start = 0
        ans = 0
        max_repeat_letters = 0
        
        for window_end, ch in enumerate(s):
            if ch not in freq_map:
                freq_map[ch] = 0
            freq_map[ch] += 1
            max_repeat_letters = max(max_repeat_letters, freq_map[ch])
            
            if window_end - window_start + 1 - max_repeat_letters > k:
                left_ch = s[window_start]
                freq_map[left_ch] -= 1
                window_start += 1
            ans = max(ans, window_end - window_start + 1)
        return ans