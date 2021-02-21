class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False     
class Trie():
    def __init__(self):
        """
        Initialize Trie DS
        """
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        ## insert words into Trie
        trie = Trie()
        for letter in words:
            trie.insert(letter)
        
        ## dfs
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                self.dfs(board, trie.root, r, c, "", res)
        
        return res
    
    def dfs(self, board, node, r, c, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        ## truncate 
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
            return
        
        curr = board[r][c]
        
        ## if curr not in Trie
        if not node:
            return 
        if curr in node.children:
            ## for search
            board[r][c] = "#"
            node = node.children.get(curr)
            self.dfs(board, node, r+1, c, path+curr, res)
            self.dfs(board, node, r-1, c, path+curr, res)
            self.dfs(board, node, r, c+1, path+curr, res)
            self.dfs(board, node, r, c-1, path+curr, res)
            ##backtracking
            board[r][c] = curr