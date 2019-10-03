# https://leetcode.com/problems/single-number/
# easy

# my approach, it is not effective comparing with best solutions
class Solution:
    def singleNumber(self, nums) -> int:
        
        arr_hash = dict()
        len_arr = len(nums)
        
        # Using hash, if v == 1, return key.(if 출현수 1개, return 해당 숫자)
        
        for i in range(len_arr):
            e = nums.pop()
            if e in arr_hash:
                arr_hash[e] += 1
            else:
                arr_hash[e] = 1
        
        for k, v in arr_hash.items():
            if v == 1:
                return k


#  Best solution using hash
# Time complexity = n , space complexity = n
'''
class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
'''

# using Math. concept: 2∗(a+b+c)−(a+a+b+b+c)=c
# 문제에서 추가 메모리 없이 풀 수 있냐고 물었는데, 이 방식은 set으로 인해 메모리 n을 추가로 소모함.
# sum 하는데 n 시간 필요하므로, time complexity도 O(2n) -> O(n)
'''
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

'''
