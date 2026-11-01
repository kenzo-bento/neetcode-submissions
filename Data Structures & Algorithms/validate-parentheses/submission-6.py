class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', "}" : "{", "]" : "["}
        stack = []
        for char in s:
            if char in ['[', "(", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif mapping[char] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True
                