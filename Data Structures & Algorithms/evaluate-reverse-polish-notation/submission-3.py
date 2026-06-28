class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                x = int(stack[-1])
                stack.pop()
                y = int(stack[-1])
                stack.pop()

                if token == "+":
                    z = y + x
                elif token == "-":
                    z = y - x
                elif token == "*":
                    z = y * x
                else:
                    z = int(y /x)

                stack.append(z)
        return int(stack[-1])