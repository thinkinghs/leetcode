
# https://leetcode.com/problems/container-with-most-water/
# medium difficulty
# Good problem

class Solution:
    def maxArea(self, height):
        height = [1,8,6,2,5,4,8,3,7]
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
