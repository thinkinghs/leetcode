
# https://leetcode.com/problems/container-with-most-water/
# medium difficulty
# Good problem

# 내 고유 솔루션
# Idea: maxarea는 height가 낮은 값과 width에 의해 결정됨.
# 가장 높은 height 값을 갖고 있는 index부터 시작 -> height을 차례대로 낮춰가면서 가장 높은 height의 index들 바깥에 있는지 확인하고, 바깥에 있으면 width에 의해 maxArea가 생길 수 있으므로 index위치를 변경하며 maxArea를 계속 탐색 함 
# 1. height arr를 내림차순으로 정렬해서 sorted_element에 assign -> 가장 높은 height부터 뽑아내려고.
# 2. height arr로 hash function 만듬, key - height값, value - 해당 height값을 갖고 있는 index들
# 3. for loop으로 가장 높은 height 부터 key를 받아오면서 현재의 exterior most lines 보다 밖에 위치해 있는지 확인
# 4. p1은 왼쪽, p2는 오른쪽. 
# 5. height가 낮아지므로 width가 넓어져야 maxarea 가능성이 있고, 
# 가장 width가 넓은 pointer를 구해야 하므로 해당 key의 value가 갖고 있는 index list에서 가장 첫째값과 마지막 값이 기존 p1과 p2보다 바깥에 있는지 확인
# 남은 width로 maxarea를 도출하기 위해 필요한 height가 height arr에 있는 최대 높이보다 높다면 더 이상 탐색 의미 없음

class Solution:
    def maxArea(self, height):
        sorted_element = sorted(list(set(height)), reverse = True)
                
        height_hash = dict()
        
        for i in range(len(height)):
            if height[i] in height_hash:
                height_hash[ height[i] ].append(i)
            else:
                height_hash[ height[i] ] = list()
                height_hash[ height[i] ].append(i)
        
        maxArea = 0
        p1 = height_hash[sorted_element[0]][0]
        p2 = height_hash[sorted_element[0]][-1]
        maxArea = (p2-p1) * sorted_element[0]
        
        for key in sorted_element:
            temp_p1 = height_hash[key][0]
            temp_p2 = height_hash[key][-1]
            if temp_p1 < p1:
                p1 = temp_p1
            if temp_p2 > p2:
                p2 = temp_p2
            
            if maxArea < (p2 - p1) * key:
                maxArea = (p2 - p1) * key
            
        return maxArea
        
    '''
        max_water = 0
        max_h = max(height)
        len_h = len(height)
        
        for i in range(len(height)-1):
            for j in range(i+1):
                h_constraint = max_water / (len_h - i-1)
                if h_constraint > max_h:
                    return max_water
                if height[j] > h_constraint and height[j-i-1] > h_constraint:
                    max_water = min(height[j], height[j-i-1]) * (len_h-i-1)
                print(max_water, i, j)
        return max_water
    '''
s = Solution()
s.maxArea(height)
height = [1,8,6,2,5,4,8,3,7]


# Solution written by a editor
# 바깥에서부터 안쪽으로 move inward 함.
# maxarea는 낮은 height에 영향을 받으므로, left와 right index 중 낮은 height를 안쪽으로 움직여야 height를 높일 수 있게 됨
# 낮은 height를 inward했을 때 더 낮은 height가 나올 수 있지만, 낮은 height를 inward하지 않으면 더 높은 height를 기대할 수조차 없기 때문에 낮은 height를 inward 해야 함 
class BestSolution:
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1
        maxheight = max(height)
        while left < right:
            maxarea = max(maxarea, min(height[left], height[right]) * (right-left))
            # 남은 width로 maxarea를 도출하기 위해 필요한 height가 height arr에 있는 최대 높이보다 높다면 더 이상 탐색 의미 없음
            # solution에는 없으나 내가 추가했고 속도 빨라짐. 상위 25%에서 상위 5%로 상승
            if maxheight < maxarea / (right-left):
                break
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxarea
