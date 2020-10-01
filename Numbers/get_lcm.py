"""
HCF = highest common factor
LCM = (num1 * num2)/HCF(num1, num2)
"""

num1 = 14
num2 = 8

smaller = min(num1, num2)
hcf = 1
for i in range(1, smaller+1):
    if (num1%i == 0 and num2%i == 0):
        hcf = i
lcm = (num1 * num2)/hcf
print("LCM of {} and {} is {}".format(num1, num2, lcm))
print("HCF of {} and {} is {}".format(num1, num2, hcf))