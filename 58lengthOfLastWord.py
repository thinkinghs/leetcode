# https://leetcode.com/problems/length-of-last-word/
# easy

class Solution:
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        
        # s = 'a ' 처럼 공백이 뒤에 있는 case가 있어서 strip 시킨 후 split 해야 됨.
        # 맨 뒤에 공백이 있으면 split(' ')했을 때 ''값이 list안에 들어가게 됨                
        return len(s.strip().split(' ')[-1])        

s = 'Hello World'
