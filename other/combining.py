# list -> listof list
# 2 ** len(ls)
def powerset(ls):
    if len(ls) == 0:
        return [[]]
    ret = []
    for subset in powerset(ls[1:]):
        ret.append(subset)
        ret.append([ls[0]] + subset)
    return ret

powerset([1,2,3])
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# list, int -> listof list[int]
# len(ls)! / (len(ls) − n)!
def permute(ls, n):
    if n == 0:
        return [[]]
    ret = []
    for i in range(len(ls)):
        for permutation in permute(ls[:i] + ls[i+1:], n-1):    #*
            ret.append([ls[i]] + permutation)
    return ret

permute([1,2,3], 2)
[[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]


# list, int -> listof list[int]
# len(ls) ** n
def permute_repeat(ls, n):
    if n == 0:
        return [[]]
    ret = []
    for i in range(len(ls)):
        for permutation in permute_repeat(ls, n-1):            #*
            ret.append([ls[i]] + permutation)
    return ret

permute_repeat([1,2,3], 2)
[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


# list, int -> listof list[int]
# len(ls)! / n! * (len(ls) − n)!
def combine(ls, n):
    if n == 0:
        return [[]]
    if ls == []:
        return []
    ret = combine(ls[1:], n)
    for combination in combine(ls[1:], n-1):      #*
        ret.append(ls[:1] + combination)
    return ret

combine([1,2,3], 2)
[[2, 3], [1, 3], [1, 2]]


# list, int -> listof list[int]
# (len(ls) + n - 1)! / n! * (len(ls) − 1)!
def combine_repeat(ls, n):
    if n == 0:
        return [[]]
    if ls == []:
        return []
    ret = combine_repeat(ls[1:], n)
    for combination in combine_repeat(ls, n-1):   #*
        ret.append(ls[:1] + combination)
    return ret

combine_repeat([1,2,3], 2)
[[3, 3], [2, 3], [2, 2], [1, 3], [1, 2], [1, 1]]
