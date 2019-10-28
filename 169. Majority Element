# https://leetcode.com/problems/majority-element/solution/

class Solution:
    def majorityElement(self, nums) -> int:
        
        major = len(nums) / 2
        majority_hash = dict()
        
        for i in nums:
            if i in majority_hash:
                majority_hash[i] += 1
                if majority_hash[i] > major:
                    return i
            else:
                majority_hash[i] = 1

nums = [3,2,3]
s = Solution()
s.majorityElement(nums)

# best practice
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        # counts.keys 로 counts의 element를 추출하여 key로 넘겨줌. max값을 추출하는 기준인 key는 get function으로 만듬.
        # counts.get( ) 은 parameter로 넘어오는 element의 개수를 return 해줌.
        return max(counts.keys, key = counts.get)
