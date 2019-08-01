# https://leetcode.com/problems/search-insert-position/submissions/

import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
'''
    # bisect_left 알고리즘 직접 구현
    # https://github.com/python/cpython/blob/master/Lib/bisect.py
    def bisect_left(self, arr, x, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(arr)
        
        # arr[mid] 와 insert할 x 값이 같을 때 x 위치를 arr[mid]의 왼쪽에 둘지 오른쪽에 둘지는 arr[mid] == x 인 경우 어떻게 처리하냐에 달라짐
        # 해당 mid 위치를 lo로 하면 mid 값이 점점 커져서 x값이 mid의 오른쪽에 위치하게 되고, 해당 mid 위치를 hi로 하면 mid 값이 점점 작아져서 x값이 mid의 왼쪽에 위치하게 됨
        while lo < hi:
            mid = (lo+hi) // 2
            if arr[mid] < x: lo = mid+1
            else: hi = mid
        return lo
 '''
