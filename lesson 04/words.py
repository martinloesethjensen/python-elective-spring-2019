# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Words exercise
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
Use str.split() (no arguments) to split on all whitespace.
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys


def words_to_dict(filename):
    words_count = {}

    file = open(filename, "r")

    for line in file:
        words = line.split()  # default is spaces

        for word in words:
            word.lower()
            words_count[word] = 1 if word not in words_count else words_count[word] + 1

    file.close()
    return words_count


###
# function that prints out the words and their count in a sorted order(biggest count),
# it can also take on a top parameter so it only prints the count given as parameter.
###
def print_words(filename, top=-1):
    words_dict = words_to_dict(filename)
    words = [(key, words_dict[key]) for key in sorted(words_dict, key=words_dict.get, reverse=True)]

    for key, value in words[:top]:
        print(key, value)


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    # Uncomment these lines to see results

    ###

    # print(words_to_dict("files/small.txt"))
    # print(words_to_dict("files/alice.txt"))

    # print_words("files/small.txt")
    # print_words("files/small.txt", top=5)
    print_words("files/alice.txt", top=20)


if __name__ == '__main__':
    main()
