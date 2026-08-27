class Solution:
    def isValid(self, s: str) -> bool:

        swap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        
        if len(s) % 2 == 1:
            return False
        
        stack = []

        for char in s:
            if char in swap:
                if stack and swap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        
        if not stack:
            return True
        else:
            return False
        
        