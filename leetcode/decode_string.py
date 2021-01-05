# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain
# any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Example 1:
#   Input: s = "3[a]2[bc]"
#   Output: "aaabcbc"

# Example 2:
#   Input: s = "3[a2[c]]"
#   Output: "accaccacc"

# Example 3:
#   Input: s = "2[abc]3[cd]ef"
#   Output: "abcabccdcdcdef"

# Example 4:
#   Input: s = "abc3[cd]xyz"
#   Output: "abccdcdcdxyz"

# Constraints:
#   1 <= s.length <= 30
#   s consists of lowercase English letters, digits, and square brackets '[]'.
#   s is guaranteed to be a valid input.
#   All the integers in s are in the range [1, 300].

class Solution:
    def decodeString(self, theinput: str) -> str:

        def decode(theinput, ret):
            if len(theinput) == 0:
                return ret
            if theinput[0].isalpha():
                return decode(theinput[1:], ret + theinput[0])
            if theinput[0].isdigit():
                # the num to be multiplied and the index of the first non digit char
                num, ind = splitnum(theinput)
                # the first bracketed expression and the rest of the input string
                thebracket, therest = splitbracket(theinput[ind:])
                return decode(num * thebracket + therest, ret)

        def splitnum(theinput):
            num = ""
            for i in range(len(theinput)):
                if theinput[i].isdigit():
                    num += theinput[i]
                else:
                    return [int(num), i]

        def splitbracket(theinput):
            ret = ["", ""]
            bracketcount = 1
            for i in range(1, len(theinput)):
                if theinput[i] == "[":
                    bracketcount += 1
                elif theinput[i] == "]":
                    bracketcount -= 1
                if bracketcount == 0:
                    ret[1] = theinput[i+1:]
                    return ret
                else:
                    ret[0] += theinput[i]

        return decode(theinput, "")
