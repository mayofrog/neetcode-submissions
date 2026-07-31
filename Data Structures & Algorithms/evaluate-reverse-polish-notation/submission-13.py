class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                a2 = stack.pop()
                a1 = stack.pop()

                if t == "+":
                    stack.append(a1 + a2)
                elif t == "-":
                    stack.append(a1 - a2)
                elif t == "*":
                    stack.append(a1 * a2)
                else:
                    stack.append(int(a1 / a2))

        return stack[-1]