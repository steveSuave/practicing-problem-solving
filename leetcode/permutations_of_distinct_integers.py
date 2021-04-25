# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if len(nums)==0:
            return [ret]
        for element in nums:
            for permutation in \
              Solution.permute(self, list(filter(lambda e: e!=element, nums))):
                ret.append([element]+permutation)
        return ret
