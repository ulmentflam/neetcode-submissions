class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        stack: List[str] = [] # Really list of chars

        def dfs(open_n, close_n):
            if open_n == close_n == n: # At the depth of both open and closed parens
                res.append("".join(stack))
                return
            
            if open_n < n: # Traverse the open tree first
                stack.append("(") # Append the opening paren to the stack
                dfs(open_n + 1, close_n) # traverse the open paren appended half of the tree
                stack.pop() # Conclude search by removing it
            if close_n < open_n: # Traverse the close tree while we have parens left unclosed.
                stack.append(")") # Append the close paren to the stack
                dfs(open_n, close_n + 1) # Traverse the close parend half of the tree
                stack.pop() # Conclude by removal
        dfs(0,0)
        return res
            