# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        n= 3
        
        result = list()
        result.append(list())
        result[0].append('(')
        
        for i in range(1, 2*n):
            result.append(list())
            for parentheses in result[i-1]:
                if( parentheses.count('(') >= n ):
                    result[i].append(parentheses + ')')
                elif( parentheses.count('(') == parentheses.count(')') ):
                    result[i].append(parentheses + '(')
                elif( parentheses.count('(') < n ):
                    result[i].append(parentheses + '(')
                    result[i].append(parentheses + ')')
        
        return result[2*n-1]
