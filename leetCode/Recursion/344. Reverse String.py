#344. Reverse String

class Solution(object):
    def reverse(self, s, index):
        if index>=len(s)//2:
            return
        
        s[index], s[len(s)-index-1]=s[len(s)-index-1], s[index]
        
        self.reverse(s, index+1)
        
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0)
        
# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         if len(s)==1:
#             return s
#         return self.reverseString(s[1:])+[s[0]]
