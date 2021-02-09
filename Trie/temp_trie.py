# Modified: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# nice code: https://gist.github.com/reterVision/8551554

#https://tutorialedge.net/compsci/data-structures/getting-started-with-tries-in-python/
from typing import Tuple
from collections import defaultdict

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = defaultdict()
        # Is it the last character of the word.
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1

def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:  #hackathon
        #found_in_child = False
        if char in node.children:
            child = node.children[char]
            child.counter += 1
            node = child
            #found_in_child = True
        # # We did not find it so add a new chlid
        # if not found_in_child:
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        if node.children.get(char):
            char_not_found = False
            child = node.children[char]
            node = child
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter

def search(root, key: str) -> bool:
    node = root
    for char in key:
        if not node.children.get(char):
            break
        child = node.children.get(char)
        node = child
    if node.word_finished:
        return True
    return False

def print_all(root, res=""):
    if not root.children and root.word_finished:
        print(res)
        return
    for child, node in root.children.items():
        #print(child, vars(node))
        res = res + child
        print_all(node, res)
        if root.char == "*":  #hkjhjhacn reinitaize res
            res = ""

def delete_word(root, key):
    ### search for node return parent n child to delete
    parent = None
    node = root
    for ch in key: #hack
        if ch not in node.children.keys():
            return "Not Found "
        parent = node
        node = node.children.get(ch)

    if node.word_finished:
        node.word_finished = False
        print("Remove node: ({})  parent {}".format(node.char, parent.char))
    else:
        print("we can't remove node")

def print_bottom_up(root):
    if not root:
        return
    for child, node in root.children.items():
        print_bottom_up(node)
        if node.char:
            print(child, end="")
    print()



if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    #add(root, "hackwwww")
    #add(root, 'kjhjhacn')

    # print(find_prefix(root, 'hac'))
    # print(find_prefix(root, 'hack'))
    # print(find_prefix(root, 'hackathon'))
    # print(find_prefix(root, 'ha'))
    # print(find_prefix(root, 'hammer'))
    #print(search(root, "hackathon"))

    # add(root, "geek")
    # add(root, "geeks")
    # add(root, 'gate')

    #print_all(root, res="")
    # delete_word(root, "kjhjhacn")
    # print_all(root, res="")
    # print(search(root, "hackathon"))
    # print(search(root, "kj"))
    print_bottom_up(root)
