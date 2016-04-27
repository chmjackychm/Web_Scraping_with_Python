# I. Regular expression for email address (from Chapter 2)

# Rule 1: [A-Za-z0-9\._+]+
#
# The first part of an email address contains at least one of the
# following: uppercase letters,lowercase letters, the numbers 0-9,
# periods (.), plus signs (+), or underscores (_).

# Rule 2: @
# After this, the email address contains the @ symbol.

# Rule 3: [A-Za-z]+
# The email address then must contain at least one uppercase or lowercase letter.

# Rule 4: \.
# This is followed by a period(.).

# Rule 5: (com|org|edu|net)
# Finally, the email address ends with com, org, edu, or net (in reality, there
# are many possible top-level domains, but, these four should suffice for the sake of example).

# By concatenating all of the rules, we arrive at the regular expression:
#    [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)


# II. Commonly used regular expression symbols
# *     -- Matches the preceding character, subexpression, or bracketed character, 0 or more times
# +     -- Matches the preceding character, subexpression, or bracketed character, 1 or more times
# []    -- Matches any character within the brackets (i.e., “Pick any one of these things”)
# ()    -- A grouped subexpression (these are evaluated first, in the “order of operations” of regular expressions)
# {m,n} -- Matches the preceding character, subexpression, or bracketed character between m and n times (inclusive)
# [^]   -- Matches any single character that is not in the bracke
# |     -- Matches any character, string of characters, or subexpression, separated by the “I” (note that this is a vertical bar, or “pipe,” not a capital “i”)
# .     -- Matches any single character (including symbols, numbers, a space, etc.)
# ^     -- Indicates that a character or subexpression occurs at the beginning of a string
# \     -- An escape character (this allows you to use “special” characters as their literal meaning)
# $     -- Often used at the end of a regular expression, it means “match this up to the end of the string.”
# ?!    -- “Does not contain.” This odd pairing of symbols, immediately preceding a character (or regular expression), indicates that that character should
#          not be found in that specific place in the larger string.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# image html structure is <img src="../img/gifts/img6.jpg">
# re.compile() --  a regular expression pattern, returning a pattern object.
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html.read())
images = soup.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

# III. Lambda Expressions
# Essentially, a lambda expression is a function that is passed into another function as a
# variable; that is, instead of defining a function as f(x, y), you may define a function as
# f(g(x), y), or even f(g(x), h(x)).
#
# BeautifulSoup allows us to pass certain types of functions as parameters into the fin
# dAll function. The only restriction is that these functions must take a tag object as an
# argument and return a boolean.
#
# For example, the following retrieves all tags that have exactly two attributes:

two_tag = soup.findAll(lambda tag: len(tag.attrs) == 2)
print(two_tag)
