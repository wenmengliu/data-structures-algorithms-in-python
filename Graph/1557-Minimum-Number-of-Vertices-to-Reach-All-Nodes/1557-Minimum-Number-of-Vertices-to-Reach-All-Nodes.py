class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        end = set(j for i, j in edges) 
        ans = []
        for i in range(n):
            if i not in end:
                ans.append(i)
        return ans