

def find_no(no):
    rem = no%10
    if rem >= 5:
        ans = no + (10-rem)
        print(("Result: ",ans))
    else:
        ans = no - rem
        print(("Result: ",ans))

nos = [4722,38,10]
for no in nos:
    find_no(no)
