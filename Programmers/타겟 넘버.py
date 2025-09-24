import sys
sys.setrecursionlimit(10**7)

# 단순하게 생각하기 -> 모든 경우 = (+ 경우의 수) + (- 경우의 수)

def solution(numbers, target):
    
    def func(idx, sum_res):
        
        if idx == len(numbers):
            if sum_res == target:
                return 1
            else:
                return 0
        
        return func(idx + 1, sum_res + numbers[idx]) + func(idx + 1, sum_res - numbers[idx])
        
        
    
    return func(0, 0) # idx, sum_res  
    
    