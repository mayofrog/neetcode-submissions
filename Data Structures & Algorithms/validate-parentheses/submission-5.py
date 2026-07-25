class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s :
            if stack and 0 < ord(c) - ord(stack[-1])  <= 2:
                stack.pop()
            else:
                stack.append(c)

        return False if stack else True

