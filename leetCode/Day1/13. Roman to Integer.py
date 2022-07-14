#13. Roman to Integer
#로마숫자가 의미하는 수 구하기

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #roman string dictionary
        roman_dict={"I":1, "V":5, "X":10, "L":50,
                    "C":100, "D":500, "M":1000}

        #result
        roman_int=0
        roman_max=0
        
        #If roman_str is smaller than previous roman, subtract from result
        for roman_str in s[::-1]:
            if roman_max<=roman_dict[roman_str]:
                roman_max=roman_dict[roman_str]
                roman_int+=roman_dict[roman_str]
            else:
                roman_int-=roman_dict[roman_str]

        return roman_int

a=Solution()
print(a.romanToInt("MCMXCIV"))
