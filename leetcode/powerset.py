# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if len(nums) == 0:
            return [ret]
        for i in Solution.subsets(self, nums[1:]):
            ret.append(i)
            ret.append([nums[0]]+i)
        return ret