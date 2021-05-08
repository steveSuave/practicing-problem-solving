// Given an array of n integers nums, a 132 pattern is a subsequence of three integers
// nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
// Return true if there is a 132 pattern in nums, otherwise, return false.

// Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

// Example 1:
// Input: nums = [1,2,3,4]
// Output: false
// Explanation: There is no 132 pattern in the sequence.

// Example 2:
// Input: nums = [3,1,4,2]
// Output: true
// Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

// Example 3:
// Input: nums = [-1,3,2,0]
// Output: true
// Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

// Constraints:

//     n == nums.length
//     1 <= n <= 10^4
//     -10^9 <= nums[i] <= 10^9

func find132pattern(nums []int) bool {
	
	// possible_mid is either the minimum 64bit integer or
	// a num smaller than some previous element of the list
	possible_mid := -9223372036854775808
	
	// bigs is a stack which will always contain at index 0 the largest element
	// already seen in the list, starting with the lists last element and
	// augmenting with decreasing numbers
	bigs := make([]int,0)
	
	for i := len(nums)-1; i > -1; i-- {
		// possible_mid > MinInt is only possible
		// if some larger number is already seen
		if nums[i] < possible_mid {
			return true
		}
		// if we see a bigger element than the stacks last (smallest)
		for len(bigs) != 0 && nums[i] > bigs[len(bigs)-1] {
			// we pop the smallest elements updating possible_mid with
			// the second-biggest to the new max available value,
			// bigs[0] might or might not get updated with the new max
			possible_mid, bigs = bigs[len(bigs)-1], bigs[:len(bigs)-1]
		}
		// the stack will always be in decreasing order
		// and possible_mid will always be smaller than bigs[0]
		bigs = append(bigs, nums[i])
	}
	return false
}
