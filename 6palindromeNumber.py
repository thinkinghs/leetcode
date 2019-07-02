class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        '''
        In order to call the str function one time, use 2 lines
        s = str(x)
        return s == s(x)[::-1]
        '''
