"""
Input:  1/2 + 3/2
Output: 2/1

"""
def get_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

def get_lcm(d1,d2):
    lcm = (d1*d2)//get_hcf(d1,d2)
    return lcm

def add_fraction(n1,d1,n2,d2):
    d3 = get_lcm(d1,d2)
    n3 = (n1 * (d3//d1)) + (n2 * (d3//d2))
    gcd_n3_d3 = get_hcf(n3, d3)
    print((n3//gcd_n3_d3, d3//gcd_n3_d3))

print((add_fraction(384 ,887 ,778 ,916)))