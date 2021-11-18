# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        def buildGraph(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)

            if child.left:
                buildGraph(child, child.left)
            if child.right:
                buildGraph(child, child.right)

        buildGraph(None, root)
        queue=[target.val]
        seen = set([target.val])
        
        for i in range(k):
            currentLevel = []
            levelSize = len(queue)
    
            for _ in range(levelSize):
                node = queue.pop()
                for neighb in graph[node]:
                    if neighb not in seen:
                        seen.add(neighb)
                        currentLevel.append(neighb)
            queue= currentLevel
        return queue