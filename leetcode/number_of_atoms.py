# Given a chemical formula (given as a string), return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
# Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
# Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

# Example 1:
#   Input: formula = "H2O"
#   Output: "H2O"
#   Explanation: The count of elements are {'H': 2, 'O': 1}.

# Example 2:
#   Input: formula = "Mg(OH)2"
#   Output: "H2MgO2"
#   Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

# Example 3:
#   Input: formula = "K4(ON(SO3)2)2"
#   Output: "K4N2O14S4"
#   Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

# Example 4:
#   Input: formula = "Be32"
#   Output: "Be32"

# Constraints:
#   1 <= formula.length <= 1000
#   formula consists of English letters, digits, '(', and ')'.
#   formula is always valid.

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def main(formula):
            return formatoutput(dictify(multgroups(listify(formula))))

        def listify(formula):
            l = []
            i = 0
            while i < len(formula):
                c = formula[i]
                if c == "(" or c == ")":
                    l.append(c)
                    i += 1
                if c.isupper():
                    atom = c
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        atom += formula[i]
                        i += 1
                    l.append(atom)
                    if (i < len(formula) and not formula[i].isdigit()) or \
                       (i == len(formula) and formula[i-1].isalpha()):
                        l.append(1)
                if c.isdigit():
                    num = c
                    i += 1
                    while i < len(formula) and formula[i].isdigit():
                        num += formula[i]
                        i += 1
                    l.append(int(num))
            return l

        def multgroups(formula):
            result = formula
            for i in range(len(result) -1, -1, -1):
                if result[i] == ")":
                    multiplier = 1
                    paren = 1
                    result[i] = None
                    if i+1 < len(result) and \
                       isinstance(result[i+1], int):
                         multiplier = result[i+1]
                         result[i+1] = None
                    j = i
                    while True:
                        j -= 1
                        if result[j] == "(":
                            paren -= 1
                        if result[j] == ")":
                            paren += 1
                        if paren > 1:
                            continue
                        if isinstance(result[j], int):
                            result[j] *= multiplier
                        if paren == 0:
                            result[j] = None
                            break
            return list(filter(None, result))

        def dictify(formula):
            result={}
            for i in range(0, len(formula)-1, 2):
                if formula[i] in result:
                    result[formula[i]] += formula[i+1]
                else:
                    result[formula[i]] = formula[i+1]
            return result

        def formatoutput(dic):
            ret = ""
            for e,cnt in sorted(dic.items()):
                ret += e
                if cnt > 1:
                    ret += str(cnt)
            return ret

        return main(formula)
