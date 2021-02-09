"""
Problem: count of character 
        in-order of occurence
        odd frquency
        prime frequency
        even frequency

"""
from collections import OrderedDict
input = "geeksforgeeks"

hash = OrderedDict({})
# Creation of hash map
for letter in input:
    hash[letter] = hash.get(letter, 0) + 1

# Print character count in-order of occurence
def in_order_occurence():
    print("In-order occurence")
    for i in hash:
        print("%s%s" % (i, hash[i]), end=' ')

# Print character count odd of occurence


def odd_occurence():
    print("\nodd occurence")
    for i in hash:
        if hash[i] % 2 != 0:
                print("%s" % i, end=' ')

# Print character count odd of occurence


def even_occurence():
    print("\neven occurence")
    for i in hash:
        if hash[i] % 2 == 0:
                print("%s" % i, end=' ')


def get_prime_nos(N):
    prime = [True]*(N+1)
    p = 2
    while p*p <= N:
        for i in range(p*p, N+1, p):
            prime[i] = False
        p += 1
    p_list = []
    for i in range(2, N+1):
        if prime[i] == True:
            p_list.append(i)
    return p_list

# # Print character count odd of occurence
def prime_occurence():
    print("\nPrime occurence")
    list_p = get_prime_nos(len(input)-1)
    for i in list_p:
        print("%s%s" % (input[i], hash[input[i]]), end=' ')



prime_occurence()