class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
              
        queue = deque([root])
        result = []
        curr_level = 0

        while queue:
            n = len(queue)
            curr_result = []


            for _ in range(n):
                node = queue.popleft()
                curr_result.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_level % 2 == 0:
                result.append(curr_result) 
            else: 
                result.append(curr_result[::-1])

            curr_level += 1
     
        return result