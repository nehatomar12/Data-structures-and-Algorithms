"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers

Given a number n, the task is to find n’th Ugly number.

"""

def is_ugly(num):
    for i in (2, 3, 5):
        while num%i == 0:
            num /= i
    return True if num == 1 else False

get_ugly_number = 150

count = 1
i = 1
while get_ugly_number > count:
    i += 1
    if is_ugly(i):
        count += 1

print(("{}’th Ugly number is {} ".format(get_ugly_number, i)))