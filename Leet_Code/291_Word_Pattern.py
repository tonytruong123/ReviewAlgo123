'''
Given a pattern and a string s, return true if s matches the pattern.
A string s matches a pattern if there is some bijective mapping of single
characters to strings such that if each character in pattern is replaced by the
string it maps to, then the resulting string is s. A bijective mapping means
that no two characters map to the same string, and no character maps to two different strings.

cat -> a
dog -> a
=> FALSE

a -> dog
a -> cat
=> FALSE
'''

