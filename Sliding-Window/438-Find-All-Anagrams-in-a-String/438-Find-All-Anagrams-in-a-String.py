class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        result_indexes = []
        pattern_count = Counter(p)
        matched = 0
        window_start = 0
        
        for window_end, ch in enumerate(s):
            if ch in pattern_count:
                pattern_count[ch] -= 1
                if pattern_count[ch] == 0:
                    matched += 1
    
            if matched == len(pattern_count):
                result_indexes.append(window_start)
    
            # shrink the sliding window by one element
            if window_end - window_start + 1 == len(p):
                left_ch = s[window_start]
                if left_ch in pattern_count:
                    if pattern_count[left_ch] == 0:
                        matched -= 1
                    pattern_count[left_ch] += 1
                window_start += 1
        return result_indexes