class Solution:
    ## hash_set
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        output = []
        word2Index = {word: i for i, word in enumerate(words)}
        for idx, w in enumerate(words):
            for j in range(len(w)+1):
                w_reversed = w[j:][::-1]
                rest = w[0:j]
                if isPalindrome(rest) and w_reversed in word2Index and word2Index[w_reversed] != idx:
                    output.append([word2Index[w_reversed], idx])
                if j == len(w): continue
                w_reversed1 = w[:j][::-1]
                rest1 = w[j:]
                if isPalindrome(rest1) and w_reversed1 in word2Index and word2Index[w_reversed1] != idx:
                    output.append([idx, word2Index[w_reversed1]])
        
        return output

def isPalindrome(word):
    return word == word[::-1]
        