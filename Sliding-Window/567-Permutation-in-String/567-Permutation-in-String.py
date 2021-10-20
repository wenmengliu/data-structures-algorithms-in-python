class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        # counter the freq of s1
        for s in s1:
            s1_freq[ord(s) - ord('a')] += 1
        
        for i, s in enumerate(s2):
            if i >= n1:
                # pop out the first character out of sliding window
                s2_freq[ord(s2[i - n1]) - ord('a')] -= 1
            # add the current index freq
            s2_freq[ord(s) - ord('a')] += 1
            if s1_freq == s2_freq:
                return True
        return False