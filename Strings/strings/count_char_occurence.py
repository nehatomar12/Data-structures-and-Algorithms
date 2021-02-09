def given_character_in_string(name="geeksforgeeks", char_to_count="g"):
    #count the occurrence of a given character in a string
    #create a map and return value of required character
    hash = {}
    for i in name:
        hash[i] = hash.get(i,0) +1
    
    if char_to_count in list(hash.keys()):
        print("%s occurs %s times" % (char_to_count, hash[char_to_count]))
    else:
        print("char not found.")

given_character_in_string()
