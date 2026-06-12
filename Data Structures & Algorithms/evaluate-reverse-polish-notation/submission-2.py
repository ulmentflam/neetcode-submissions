class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval() -> int:
            token: str | int = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            a = eval()
            b = eval()
            if token == "*":
                return a * b
            if token == "/":
                return int(float(b)/a)
            if token == "-":
                return b - a
            if token == "+":
                return a + b
        return eval()
        