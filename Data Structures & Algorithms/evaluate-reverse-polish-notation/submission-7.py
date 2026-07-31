class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = ["+", "-", "*", "/"]
        stack = []
        x = int(tokens[0])
        for t in tokens:
            if t not in a:
                stack.append(t)
            else:
                a2 = int(stack.pop())
                a1 = int(stack.pop())
                if t == "+":
                    x = a1 + a2
                elif t == "-":
                    x = a1 - a2
                elif t == "*":
                    x = a1 * a2
                elif t == "/":
                    x = a1 / a2
                stack.append(x)
        return int(x)
            


