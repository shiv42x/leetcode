class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
    
        def dfs(string, hanging_opens):
            if len(string) == 2 * n: 
                if hanging_opens > 0:
                    return

                results.append(string)
                return 

            if hanging_opens > 0:
                dfs(string + ')', hanging_opens - 1)
            
            dfs(string + '(', hanging_opens + 1)

        dfs("", 0)
        return results
        """
        optimal solution:

        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
        """