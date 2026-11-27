# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder_(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # DFS approach recursion
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0) 
        return res
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # BFS approach Iteration, using a queue
        if not root:
            return []
        
        queue = collections.deque() # create the queue 
        queue.append(root) # push the root

        while queue: # while the queue is not empty
            length = len(queue) # number of nodes currently in the queue
            val_level = [] # the list that will contain the values of those currents nodes
            for i in range(length): # for each node, pop it, add the value if not empty to val_level, now push its left and right children if there exists in the queue
                node = queue.popleft()
                if node:
                    val_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if val_level: # we append val_level to the resulting list
                res.append(val_level)
        return res
        