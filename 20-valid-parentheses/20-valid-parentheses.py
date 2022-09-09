class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for c in s:
            #c is a closing bracket and we haven't found a opening bracket
            if not stack and c in brackets:
                return False
            #starting bracket
            if c not in brackets:
                stack.append(c)
            #ending bracket and 
            else:
                top = stack.pop()
                if not brackets[c] == top:
                    return False
        
        return not stack
                
                