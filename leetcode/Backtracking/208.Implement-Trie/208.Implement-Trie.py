class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root 
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        ## set the lastWord as "#"
        p['#'] = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None
        
    def find(self,prefix):
        """
        Returns the trie node start of prefix. If no prefix exists in the trie,             
        return None
        :type prefix: str
        :rtype p: set
        """
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p