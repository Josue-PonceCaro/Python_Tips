import re


# Matches the contents of the group of the same number. Groups are numbered starting from 1. 
# For example, (.+) \1 matches 'the the' or '55 55', but not 'thethe' (note the space after the group). 
# This special sequence can only be used to match one of the first 99 groups. 
# If the first digit of number is 0, or number is 3 octal digits long, 
# it will not be interpreted as a group match, but as the character with octal value number. 
# Inside the '[' and ']' of a character class, all numeric escapes are treated as characters.

txt = "word fo to foffffo foffffo to to to to find"
# x = re.search("\brd\b",txt)
x = re.search(r'(to) (to) \2',txt)
print(x)
x = re.search(r'(.+) \1',txt)
print(x)


# \b
# Matches the empty string, but only at the beginning or end of a word.
#  A word is defined as a sequence of word characters. Note that formally,
#  \b is defined as the boundary between a \w and a \W character (or vice versa),
#  or between \w and the beginning/end of the string. This means that r'\bfoo\b'
#  matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
txt = "word foo to find"
# x = re.search("\brd\b",txt)
x = re.search(r'\bto\b',txt)
print(x)

# \A
# Matches only at the start of the string.
txt = "word foo to find"
# x = re.search("\brd\b",txt)
x = re.search(r'\Awor',txt)
print(x)

