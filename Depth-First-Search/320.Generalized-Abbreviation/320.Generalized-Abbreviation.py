class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        def dfs(pos, cur, cnt):
            ## when the position reaches the end of the word, add to result
            if len(word) == pos:
                cur = cur + str(cnt) if cnt > 0 else cur
                res.append(cur)
                return res
            
            ## update the current character to abbreviation and reset count to zero
            dfs(pos+1, cur + (str(cnt) if cnt>0 else "") + word[pos], 0)
            ## keep the current character
            dfs(pos+1, cur, cnt+1)
           
        dfs(0,"",0)
        return res