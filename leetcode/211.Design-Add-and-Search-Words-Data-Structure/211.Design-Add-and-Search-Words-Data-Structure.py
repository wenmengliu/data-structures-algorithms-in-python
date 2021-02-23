class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for p in word:
            if p not in node:
                node[p] = {}
            node = node[p]
        
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root 
        
        return self.dfs(word, node)
    
    def dfs(self, word, node):  
        for i, p in enumerate(word):
            if p not in node:
                # if the current character is dot ('.')
                if '.' in p:
                    for x in node:
                        if x != '#' and self.dfs(word[i+1:], node[x]):
                            return True
                # if p is not dot or no node leads to answer
                return False
            else:
                node = node[p]
        return '#' in node