st = "GeeksforGeeks"
remove_chr = "f"

print(st.replace(remove_chr,""))
print("".join([x for x in st if x != remove_chr]))
print(st.translate(None, remove_chr))


# Remove  characters from the first String which are present in the second
st1 = "India is great" 
st2 = "in"

print("".join([x for x in st1 if x.lower() not in list(st2.lower())]))