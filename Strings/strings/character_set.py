'''
Change string to a new character set
New character set : qwertyuiopasdfghjklzxcvbnm
Input : "utta"
Output : geek

Input : "egrt"
Output : code

'''
import pprint
set_given = "qwertyuiopasdfghjklzxcvbnm"
input = "utta"
original_set = ""
for i in range(97,(97+26)):
    original_set = original_set + chr(i)

def using_zip():
    new_set = dict(list(zip(set_given, original_set)))
    #new_set = dict(zip(original_set, set_given))
    pprint.pprint(new_set)
    for i in input:
        print(new_set[i], end=' ')

def with_mapp():
    index_build = {}
    # q0 w1 e2 ...
    for i in range(0, len(set_given)):
        index_build[set_given[i]] = i
    
    for i in input:
        print(original_set[index_build[i]], end=' ')

using_zip()
with_mapp()

