class WordFilter:
    def __init__(self, words: List[str]):
        # generate suffix + # + word
        self.trie = Trie()
        for i, word in enumerate(words):
            l = len(word)
            for j in range(l+1):
                self.trie.insert(word[j:l] + "_" + word, i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix + "_" + prefix)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        node = self.root
        node.weight = index
        for p in word:
            if p not in node.children:
                node.children[p] = TrieNode()
            node = node.children[p]
            node.weight = index 
    
    def search(self, word):
        node = self.root       
        for p in word:
            if p not in node.children:
                return -1
            node = node.children[p]
        return node.weight
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1