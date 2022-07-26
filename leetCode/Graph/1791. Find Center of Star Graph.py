#1791. Find Center of Star Graph

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
#         edge_num=[0 for _ in range(len(edges)+1)]
#         for i, k in edges:
#             edge_num[i-1]+=1
#             edge_num[k-1]+=1
        
#         for i in range(len(edge_num)):
#             if edge_num[i]==len(edges):
#                 return i+1
            
