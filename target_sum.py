from typing import List

def target_sum(nums: List[int], target:int):
    cache = {} # (index, total) -> # of ways to target value

    def backtrack(index, total):
        if index == len(nums):
            return 1 if total == target else 0 
        if (index, total) in cache:
            return cache[(index, total)]
        
        cache[(index, total)] = (backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index]))
        return cache[(index, total)]
    return backtrack(0,0)
nums = [1,1,1,1,1]
target = 3

print(target_sum(nums, target))

