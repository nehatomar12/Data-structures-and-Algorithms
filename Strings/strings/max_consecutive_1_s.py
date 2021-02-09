"""
Input : str = '11000111101010111'
Output : 4
"""
str1 = "11000111101010111"

str_list = str1.split('0')
print(str_list)
max_val = 0
for i in str_list:
    if i != "":
        if len(i) > max_val:
            max_val =len(i)

print(('1'* max_val))

str2 = "11000111101010111"
print((max(list(map(len,str2.split('0'))))))

