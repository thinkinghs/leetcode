# return the element list of longest substring
# leetcode just ask the length of substring, but I make a code returning the list of substring

# max substring의 element 값을 return 하는 코드, 내가 직접 만듬
# 메모리는 len값 return 하는 것와 비슷하게 사용, list 저장 공간이 기본적으로 사용되는 메모리양(릿코드에서는 13메가 정도)에 비해 미미해서 그런듯.
# runtime은 len만 계산하는거에 비해 조금 늦음. curr를 max_so_far에 저장하는 동안 n 타임이 소요되므로 그런듯
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> list:
        
        dic = dict()
        start = 0
        max_so_far = list()
        curr = list()
        
        for idx, key in enumerate(s):
            # dic[key] 에서 key error가 나지 않도록 key가 dic에 있는지 먼저 확인, 순서 중요
            if key in dic and dic[key] >= start:
                if len(max_so_far) < len(curr):
                    max_so_far = curr[:]
                start = dic[key] + 1
                # s가 str이므로 curr을 계속 list로 유지하려면 s를 slice한 값을 list로 감싸야 됨
                curr = list(s[start:idx+1])
            else:
                curr.append(key)
            dic[key] = idx
        return curr if len(max_so_far) < len(curr) else max_so_far
