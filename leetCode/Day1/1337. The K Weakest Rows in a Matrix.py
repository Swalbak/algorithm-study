#1337. The K Weakest Rows in a Matrix

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        #return array
        result_arr=[]
        
        #column index
        col=0

        #We need 0~k-1 data
        #So iterate while length of result_arr is less than k
        while len(result_arr)<k:
            for i in range(len(mat)):
                if i not in result_arr:
                    #all elements are '1'
                    if col==len(mat[i]):
                        result_arr.append(i)
                    elif mat[i][col]==0:
                        result_arr.append(i)
            col+=1
        return result_arr[:k]

mat=[[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
k=3
a=Solution()
print(a.kWeakestRows(mat, k))
