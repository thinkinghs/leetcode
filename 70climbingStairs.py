# https://leetcode.com/problems/climbing-stairs/
# easy

# 저자의 solution에 내 방법은 없음.
# 나는 combination 이용해서 경우의 수를 구함. 5의 경우의 수 구할 때 [2,1,1,1] 처럼 2가 한개이면 4c1, 2가 2개이면 [2,2,1] 로 3c2 로 구함
# n개의 위치 중 2가 위치한 자리를 뽑는다는 개념 (0,1), (0,2), (1,2) 처럼.
class Solution:
    # https://smlee729.github.io/python/algorithm/2015/03/08/1-nchoosek.html
    # 위 링크 자료 활용
    def NChooseK_fast(self, n, k):
        numerator = 1
        denominator = 1
        k = min(n-k, k) #조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
        for i in range(1, k+1):
            denominator *= i
            numerator *= n+1-i
        return numerator/denominator
    
    def climbStairs(self, n:int) -> int:
        # 2 step이 가능한 경우의 몫
        quotient = n // 2
        ways = 1
        for i in range(1, quotient+1):
            ways += self.NChooseK_fast(n-i,i)
    
        return ways

# solution에 memoization 풀이법 참고
# memo 값을 기억해 둠에 따라, 모든 경우에 recursion 할 필요 없고 memo[i] 값을 알면 바로 값을 return 받아서 사용함
class memoizationSolution:
    def climbStairs(self, n):
        memo = [0] * (n+1)
        return self.climbStairsRecursion(0, n, memo)
    
    def climbStairsRecursion(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0 :
            return memo[i]
        memo[i] = self.climbStairsRecursion(i+1, n, memo) + self.climbStairsRecursion(i+2, n, memo)
        return memo[i]
