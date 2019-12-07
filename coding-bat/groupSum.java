/*
Given an array of ints, is it possible to choose a group of 
some of the ints, such that the group sums to the given target? 
This is a classic backtracking recursion problem. 
Rather than looking at the whole array, our convention is to 
consider the part of the array starting at index start and 
continuing to the end of the array. The caller can specify the 
whole array simply by passing start as 0. No loops are needed 
-- the recursive calls progress down the array.

groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false
*/

public boolean groupSum(int start, int[] nums, int target) {
  
  if (target==0) return true;
  if (start>=nums.length) return false;
  if (contains(start, nums, target)) return true;
  
  if (nums[start]<target)
    return groupSum(start+1, nums, target-nums[start]);
  
  return groupSum(start+1, nums, target);
  
}

public boolean contains(int ind, int[] nmrs, int num){
  
  if (ind>=nmrs.length) return false;
  if (nmrs[ind]==num) return true;
  return contains(ind+1, nmrs, num);
  
}

