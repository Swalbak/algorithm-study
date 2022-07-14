#20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Par_dict={"(":")", "[":"]", "{":"}"}
        stack=[]

        for par in s:
            if par in Par_dict:
                stack.append(par)
            elif len(stack)==0 or Par_dict[stack.pop()]!=par:
                return False
        
        if len(stack)!=0:
            return False
        return True

a=Solution()
print(a.isValid("()[]{}"))
