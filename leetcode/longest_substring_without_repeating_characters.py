# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.

# Example 2:
#   Input: s = "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.

# Example 3:
#   Input: s = "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#   Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
#   Input: s = ""
#   Output: 0

# Constraints:
#   0 <= s.length <= 5 * 104
#   s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 1
        thelens = [1]
        for i in range(len(s)):
            theLetters = [s[i]]
            j = i+1
            while j < len(s):
                if s[j] != s[i] and s[j] not in theLetters:
                    theLetters.append(s[j])
                    count += 1
                else: break
                j += 1
            thelens.append(count)
            count = 1
        return max(thelens)

