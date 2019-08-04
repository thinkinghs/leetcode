# https://leetcode.com/problems/plus-one/submissions/
# easy

class Solution:
    def plusOne(self, digits):
        n = ''
        for i in digits:
            n += str(i)
        n = int(n) + 1
        result = [i for i in str(n)]
        return result
