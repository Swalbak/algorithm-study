#387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_dict={}
        
        for sp in s:
            if sp in str_dict:
                str_dict[sp]+=1
            else:
                str_dict[sp]=0
        
        for i in range(len(s)):
            if str_dict[s[i]]==0:
                return i
        return -1
                
        
#         exist_str=[]
#         queue=list(s)
#         index=0
        
#         while len(queue)!=0:
#             sp=queue[0]
#             del queue[0]
#             if sp not in queue and sp not in exist_str:
#                 return index
#             else:
#                 exist_str.append(sp)
#                 index+=1
#         return -1
        
            
