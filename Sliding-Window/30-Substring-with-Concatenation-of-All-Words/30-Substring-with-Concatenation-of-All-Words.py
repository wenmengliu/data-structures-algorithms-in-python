class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq = collections.Counter(words)
        word_count = len(words)
        word_length = len(words[0])
        res = []
        for i in range(len(s) - word_count * word_length + 1):
            words_seen = {}
            for j in range(word_count):
                next_word_index = i + j * word_length
                word = s[next_word_index: next_word_index + word_length]
                if word not in word_freq:
                    break
                
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1
                
                if words_seen[word] > word_freq.get(word):
                    break
                
                if j + 1 == word_count:
                    res.append(i)
        return res