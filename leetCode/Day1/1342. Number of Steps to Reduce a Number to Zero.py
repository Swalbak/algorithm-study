#1342. Number of Steps to Reduce a Number to Zero

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        while num!=0:
            count+=num%2+1
            num//=2

        return count-1

num=123
a=Solution()
print(a.numberOfSteps(num))
            
