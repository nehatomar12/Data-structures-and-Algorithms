"""
given_conversion = {'A': 'D','M':'P','X':'A',
                    'a':'d','m':'p','x':'a'}

a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
a-z 97-122
A-Z 65-90

cases for lower and upper
lower:  if ord(w)+3 <= 122:
           print chr(ord(w)+3)
        else:
            bits = ord(w)+3 - 122
            print chr(96+bits)
"""
inp = "Vrphwklqj phdqlqjixo"
inp = "Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw dudqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg <= 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj. Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu dojrulwkp"
arr =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ['(',')','.',',','>','=','<','=', '/', ' ']
N=3
new_arr = arr[-N:] + arr[:-N]
res = ""
for l in inp:
    if l in special or l.isnumeric():
        res = res + l
    elif l.isupper():
        res = res + new_arr[ord(l) - 65]
    else:
        res = res + new_arr[ord(l) - 97]

print(res)
