
word_set = " This is a series of strings to count " \
   "many words . They sometime hurt and words sometime inspire "\
   "Also sometime fewer words convey more meaning than a bag of words "\
   "Be careful what you speak or what you write or even what you think of. "\

from collections import Counter
words = word_set.split()
# List of all words with count ('words', 4), ('sometime', 3), ('what', 3) ..
print(Counter(words).most_common())

hash = {}
max_count = 0
max_word = ""
for word in words:
    hash[word] = hash.get(word, 0) + 1
    if hash[word] > max_count:
        max_count = hash[word]
        max_word = word
print("{} occurs {} times".format(max_word, max_count))