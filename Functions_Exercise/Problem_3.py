#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def string_compare(string_1, string_2):
    len_string_1 = len(string_1)
    len_string_2 = len(string_2)
    len_strings =abs(len_string_1 - len_string_2)
    if string_1[0] == string_2[len_strings] and string_1[1] == string_2[len_strings+1]:
        return True



string_1 = "hi"
string_2 = "2hi"
b = string_compare(string_1, string_2)
print(b)

print(len("hi2"))