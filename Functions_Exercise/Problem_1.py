#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

my_list = [4, 5,4, 6, 7,1,2,3]


def array_check(checklist):
    num_list = [1, 2, 3]
    for i in range(len(checklist)):
        if checklist[i] == 1 and checklist[i+1] == 2 and checklist[i+2] == 3:
            return True

    return False


print(array_check(my_list))


