
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
    

class bestSolution:
    def letterCombination(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination and append (proceed to the next digits) 문법적으론 안 맞는데, 다음 digit 나아가는 부분을 추가하라 라는 의미로 저자가 쓴 듯 
                    backtrack(combination + letter, next_digits[1:])
            
        # 같은 class 안에 있으면 function 밖에 있는 variable 이용 가능
        output = []
        if digits:
            backtrack("", digits)
        return output
