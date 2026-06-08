class Solution:
    def isValid(self, s: str) -> bool:
        ctrl_chars = {
            '(': '',
            ')': '(',
            '{': '',
            '}': '{',
            '[': '',
            ']': '[',
        }

        stack: List = []
        for c in s:
            if c in ctrl_chars:
                if not stack:
                    stack.append(c)
                    continue
                top = stack[-1]
                if top == ctrl_chars[c]:
                    stack.pop()
                    continue
                stack.append(c)
        return len(stack) == 0                



        