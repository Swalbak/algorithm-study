#1672. Richest Customer Wealth


class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        return max(map(lambda ary:sum(ary), accounts))

accounts=[[2,8,7],[7,1,3],[1,9,5]]
a=Solution()
print(a.maximumWealth(accounts))
