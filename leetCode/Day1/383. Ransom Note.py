class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine=list(magazine)
        for ransom in ransomNote:
            if ransom in magazine:
                magazine.remove(ransom)
            else:
                return False
            
        return True
        

a=Solution()
print(a.canConstruct("aa", "aab"))
