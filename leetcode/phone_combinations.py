# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given.
# Note that 1 does not map to any letters.

notes = [
    None,
    None,
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
    ['j','k','l'],
    ['m','n','o'],
    ['p','q','r', 's'],
    ['t','u', 'v'],
    ['w','x', 'y', 'z']
]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return notes[int(digits)]
        ret = []
        for combo in self.letterCombinations(digits[1:]):
            for char in notes[int(digits[0])]:
                ret.append(char+combo)
        return ret
