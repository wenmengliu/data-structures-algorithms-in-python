class TrieNode:
    def __init__(self):
        self.sentence = None
        self.rank = 0
        self.isEnd = False
        self.children = {}
        
        
class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        for st, t in zip(sentences, times):
            self.insert(st, t)
    
    def insert(self, sentence, time):
        cur = self.root
        for s in sentence:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        cur.isEnd = True
        cur.sentence = sentence
        cur.rank -= time
    
    def dfs(self, root):
        res = []
        if root:
            if root.isEnd:
                res.append((root.rank, root.sentence))
            for child in root.children:
                res.extend(self.dfs(root.children[child]))
        return res
    
    def search(self, sentence):
        cur = self.root
        for s in sentence:
            if s not in cur.children:
                return []
            cur = cur.children[s]
        return self.dfs(cur)
        
    def input(self, c: str) -> List[str]:
        output = []
        if c!= '#':
            self.keyword += c
            output = self.search(self.keyword)
        else:
            self.insert(self.keyword, 1)
            self.keyword = ""
        return [res[1] for res in sorted(output)[:3]]
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)