class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token.isdigit() or token.lstrip('-').isdigit():
                stack.append(token)
            else:
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()
                if token == '+':
                    stack.append(str(b + a))
                elif token == '-':
                    stack.append(str(b - a))
                elif token == '*':
                    stack.append(str(b * a))
                else:
                    stack.append(str(int(b / a)))
        return int(stack[-1])

                
                
        