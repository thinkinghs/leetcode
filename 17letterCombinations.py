
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from itertools import product
from functools import reduce
class Solution:
    def letterCombinations(self, digits: str):
        
        def digitToLetter(d):
            if d == '2':
                return 'abc'
            elif d == '3':
                return 'def'
            elif d == '4':
                return 'ghi'
            elif d == '5':
                return 'jkl'
            elif d == '6':
                return 'mno'
            elif d == '7':
                return 'pqrs'
            elif d == '8':
                return 'tuv'
            elif d == '9':
                return 'wxyz'
            else:
                raise ValueError('Not valid number')
        
        def test(*a):
            print(a)
        
        if not digits:
            return ""
        letters = [digitToLetter(i) for i in digits]
        
        test(letters)
        
        result = list()
        # product 는 2개 이상의 리스트의 모든 조합 구할 수 있음
        # letters 앞에 asterisk 하는 이유는 unpacking 하기 위함.
        # https://mingrammer.com/understanding-the-asterisk-of-python/
        # 이 부분은 공부하기
        # https://docs.python.org/3/library/itertools.html
        for each in list(product(*letters)):
            result.append(reduce(lambda a, b: a+b, each))
        return result
    
