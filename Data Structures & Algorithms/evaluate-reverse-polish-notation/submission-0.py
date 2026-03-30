class Solution:

    def calculate(self, stack: List[str], c):
        b = int(stack.pop())
        a = int(stack.pop())
        if c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)
        elif c == '*':
            stack.append(a * b)
        elif c == '/':
            stack.append(int(a / b))

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
            else:
                self.calculate(stack, token)

        return int(stack[0])