class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        for i in range(1, n+1):
            elem_str=""
            if i%3==0:
                elem_str="Fizz"
            if i%5==0:
                elem_str+="Buzz"
            if elem_str=="":
                elem_str=str(i)

            result.append(elem_str)
        return result

a=Solution()
print(a.fizzBuzz(15))
