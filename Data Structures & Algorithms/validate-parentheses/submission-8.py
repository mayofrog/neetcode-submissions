class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {')':'(', '}':'{', ']':'['}
        for c in s:
            if stack and c in a and stack[-1] == a[c]:
                stack.pop()
            else:
                stack.append(c)

        if stack: return False
        else: return True


