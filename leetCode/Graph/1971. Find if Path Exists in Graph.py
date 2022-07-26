#1971. Find if Path Exists in Graph

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if len(edges)<=1:
            return True
        
        graph=[[] for _ in range(n)]
        
        for start, des in edges:
            graph[start].append(des)
            graph[des].append(start)
        
        stack=[source]
        visited_array=[source]
        
        while len(stack)!=0:
            cur=graph[stack.pop()]
            if destination in cur:
                return True
            
            for node in cur:
                if node not in visited_array:
                    stack.append(node)
                    visited_array.append(node)
        
        return False
            
        
