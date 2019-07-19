# https://leetcode.com/problems/3sum/
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''

class Solution:
    def threeSum(self, nums):
        nums = [-1,0,1,2,-1,-4]

        hashed_arr = dict()
        
        for idx, v in enumerate(nums):
            if v in hashed_arr:
                hashed_arr[v].append(idx)
            else:
                hashed_arr[v] = [idx]
        
        items = list()
        past_hashed = dict()
        
        for i in range(len(nums)-2):
            if nums[i] in past_hashed:
                continue
            else:
                past_hashed[nums[i]] = i
            for j in range(i+1,len(nums)-1):
                k_value = -(nums[i]+nums[j])
                if k_value in hashed_arr:
                    # and any(hashed_idx > j for hashed_idx in hashed_arr[k_value]): 라고 하면 코드 가독성 좋아지지만 for문을 다 돌고 [T,T,T,T] 등의 상태에서 any를 하기 때문에 속도 느려짐. 그냥 ture 발견하면 바로 for문 break 시키는게 빠름
                    # hashed_arr[k_value] 안에 값은 nums의 index 값이고 오름차순으로 되어 있음. 그래서 뒤에서부터 뽑아서 j보다 큰지 확인하면 더 빠름 
                    for hashed_idx in hashed_arr[k_value][::-1]:
                        if hashed_idx > j:
                            items.append([nums[i],nums[j],k_value])
                            break
        
        result = list(map(list,set([tuple(sorted(item)) for item in items])))

        return result
