# Sum of Unique Elements
# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# @param {Integer[]} nums
# @return {Integer}
def sum_of_unique(nums)
    (nums.filter { |x| nums.count(x) == 1 }).sum
end
