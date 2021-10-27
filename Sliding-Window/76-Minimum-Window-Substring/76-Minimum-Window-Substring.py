class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        mini_length, substr_start = len(s) + 1, 0
        window_start = 0
        freq_t = Counter(t)
        matched = 0
        
        for window_end, ch in enumerate(s):
            if ch in freq_t:
                freq_t[ch] -= 1
                if freq_t[ch] >= 0:
                    matched += 1
            
            while matched == len(t):
                if mini_length > window_end - window_start + 1:
                    mini_length = window_end - window_start + 1
                    substr_start = window_start
                
                left_ch = s[window_start]
                window_start += 1
                
                if left_ch in freq_t:
                    if freq_t[left_ch] == 0:
                        matched -= 1
                    freq_t[left_ch] += 1
        
        return s[substr_start:substr_start + mini_length] if mini_length < len(s) + 1 else ""