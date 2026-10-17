class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_close ={")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in dict_close: # then, it is a closing parenthese
                if stack and stack[-1]==dict_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
        