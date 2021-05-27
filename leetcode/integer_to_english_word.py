# Convert a non-negative integer num to its English words representation.

# Example 1:
#     Input: num = 123
#     Output: "One Hundred Twenty Three"

# Example 2:
#     Input: num = 12345
#     Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
#     Input: num = 1234567
#     Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Example 4:
#     Input: num = 1234567891
#     Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

# Constraints:
#     0 <= num <= 231 - 1


# =============================================================================================================================
# BNF Grammar:

# ones = "" | "one" | "two" | "three" | "four" | "five" | "six" | "seven" | "eight" | "nine"
# teens = "ten" | "eleven" | "twelve" | "thirteen" | "fourteen" | "fifteen" | "sixteen" | "seventeen" | "eighteen" | "nineteen"
# tys = "twenty" | "thirty" | "fourty" | "fifty" | "sixty" | "seventy" | "eighty" | "ninety"
# tens = teens | tys ones

# 1digit   = ones
# 2digits  = tens
# 3digits  = 1digit  "hundred"  2digits
# 4digits  = 1digit  "thousand" 3digits
# 5digits  = 2digits "thousand" 3digits
# 6digits  = 3digits "thousand" 3digits
# 7digits  = 1digit  "million"  6digits
# 8digits  = 2digits "million"  6digits
# 9digits  = 3digits "million"  6digits
# 10digits = 1digit  "billion"  9digits

onesNteens = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tys = [None, None,"Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
orders = [None, None, None, None, "Thousand", "Thousand", "Thousand", "Million", "Million", "Million", "Billion"]

def ndigits(i, n):
    if n == 1:
        return onesNteens[int(i)]
    if n == 2:
        if int(i) < len(onesNteens):
            return onesNteens[int(i)]
        return tys[int(i[0])] + " " + onesNteens[int(i[1])]
    if n == 3:
        first = ndigits(i[0], 1)
        if first == "":
            return ndigits(i[1:],2)
        return first + " Hundred " + ndigits(i[1:], 2)

    x = n % 3 or 3
    start = ndigits(i[:x], x)
    if start == "":
        return ndigits(i[x:], n-x)
    return start + " " + orders[n] + " " + ndigits(i[x:], n-x)

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"        
        strint = str(num)
        n = len(strint)
        return " ".join(ndigits(strint, n).split())
