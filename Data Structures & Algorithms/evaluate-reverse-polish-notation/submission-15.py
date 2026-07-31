class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = {"+", "-", "*", "/"}
        stack = []
        
        for t in tokens:
            if t not in a:
                stack.append(int(t))
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                if t == "+":
                    x = a1 + a2
                elif t == "-":
                    x = a1 - a2
                elif t == "*":
                    x = a1 * a2
                elif t == "/":
                    x = int(a1 / a2)
                stack.append(x)
        return stack[-1]
            


