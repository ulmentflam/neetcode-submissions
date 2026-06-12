class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        This is a prime example of recursion. It will take O(n)
        space in the stack.

        Recursion is often hard to read, so I can do it with a traditional stack.
        """

        stack: List[int] = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
                continue
            a, b = stack.pop(), stack.pop()
            if c == "+":
                stack.append(a + b)
            if c == "-":
                stack.append(b - a)
            if c == "*":
                stack.append(a * b)
            if c == "/":
                stack.append(int(float(b)/a))
        return int(stack.pop())

        