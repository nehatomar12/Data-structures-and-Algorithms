
from collections import Counter
word_set = " This is a series of strings to count " \
    "many words . They sometime hurt and words sometime inspire "\
    "Also sometime fewer words convey more meaning than a bag of words "\
    "Be careful what you speak or what you write or even what you think of. "\

words = word_set.split()
# List of all words with count ('words', 4), ('sometime', 3), ('what', 3) ..
#print((Counter(words).most_common()))


def k_freuent_word():
    hash = {}
    max_count = 0
    max_word = ""
    for word in words:
        hash[word] = hash.get(word, 0) + 1
        if hash[word] > max_count:
            max_count = hash[word]
            max_word = word
    print(("{} occurs {} times".format(max_word, max_count)))


# using hash
def k_freuent_word_in_file():
    hash = {}
    max_count = 0
    max_word = ""
    with open("./data_set/frequent.txt") as f:
        for line in f.readlines():
            for word in line.split():
                hash[word] = hash.get(word, 0) + 1
                if hash[word] > max_count:
                        max_count = hash[word]
                        max_word = word
    print(("{} occurs {} times".format(max_word, max_count)))

# using Trie and minHeap
import heapq
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        self.key = None
        self.counter = 1

def make_trie(root, word, heap):
    node = root
    newWord = False
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
            newWord = True
        node = node.children.get(char)
    node.isLeaf = True
    node.key = word
    if not newWord:
        node.counter += 1
        if heap[0][0] < node.counter:
            heap[0] = (node.counter, node.key)
            heapq.heapify(heap)

def printTrie(root):
    for _, node in sorted(root.children.items()):
        if node.key:
            print((node.key, node.counter))
        printTrie(node)


def k_freuent_word_using_trie_minHeap():
    k = 2
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-1, None))

    root = TrieNode()
    with open("./data_set/frequent.txt") as f:
        for line in f.readlines():
            for word in line.split():
                make_trie(root, word, heap)

    print(heap[0])

# k_freuent_word()
k_freuent_word_in_file()
k_freuent_word_using_trie_minHeap()
