# To find the powerset of a list:
# If the list is empty then the result is the set with the empty list.
# Otherwise find the powerset of the list without the head and keep each element twice.
# Once unchanged and once having appended the head to it.
#
# list -> listof list
def powerset(xs):
    """
    2^n
    """
    if len(xs) == 0:
        return [[]]
    ret = []
    for subset in powerset(xs[1:]):
        ret.append(subset)
        ret.append([xs[0]] + subset)
    return ret

powerset([1,2,3])
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# To find the permutations of a list by k elements:
# If k is 0 the result is the set with the empty list.
# Otherwise remove one element from the list,
# find the permutations of the remaining elements by k-1
# and append to each permutation of this result the excluded element.
# Then put the excluded element back to the original list, remove the next one and
# repeat the steps until the original list is exhausted.
#
# list, int -> listof list[int]
def permute(xs, k):
    """
       n!
    --------
     (n−k)!
    """
    if k == 0:
        return [[]]
    ret = []
    for i in range(len(xs)):
        for permutation in permute(xs[:i] + xs[i+1:], k-1):    #*
            ret.append([xs[i]] + permutation)
    return ret

permute([1,2,3], 2)
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]


# To find the permutations of a list by k elements, with replacement:
# If k is 0 the result is the set with the empty list.
# Otherwise for each element, find the permutations with replacement by k-1
# of the entire original list and append to each permutation of the result
# this element.
#
# list, int -> listof list[int]
def permute_repeat(xs, k):
    """
    n^k
    """
    if k == 0:
        return [[]]
    ret = []
    for i in range(len(xs)):
        for permutation in permute_repeat(xs, k-1):            #*
            ret.append([xs[i]] + permutation)
    return ret

permute_repeat([1,2,3], 2)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]


# To find the combinations of a list by k elements:
# Firstly: if k is 0 the result is the set with the empty list,
# Secondly: if the list is empty the result is the empty list.
# otherwise the result is the combinations of the tail of the list by k elements
# together with the combinations of the *tail* by k-1 elements, where to each element
# the head has been appended.
#
# list, int -> listof list[int]
def combine(xs, k):
    """
        n!
    ----------
     k!(n−k)!
    """
    if k == 0:
        return [[]]
    if xs == []:
        return []
    ret = combine(xs[1:], k)
    for combination in combine(xs[1:], k-1):      #*
        ret.append(xs[:1] + combination)
    return ret

combine([1,2,3], 2)
# [[2, 3], [1, 3], [1, 2]]


# To find the combinations of a list by k elements with replacement:
# Firstly: if k is 0 the result is the set with the empty list,
# Secondly: if the list is empty the result is the empty list.
# otherwise the result is the combinations with replacement of the tail of the list by k elements
# together with the combinations with replacement of the *entire list* by k-1 elements,
# where to each element the head has been appended.
#
# list, int -> listof list[int]
def combine_repeat(xs, k):
    """
     (n+k-1)!
    ----------
     k!(n−1)!
    """
    if k == 0:
        return [[]]
    if xs == []:
        return []
    ret = combine_repeat(xs[1:], k)
    for combination in combine_repeat(xs, k-1):   #*
        ret.append(xs[:1] + combination)
    return ret

combine_repeat([1,2,3], 2)
# [[3, 3], [2, 3], [2, 2], [1, 3], [1, 2], [1, 1]]
