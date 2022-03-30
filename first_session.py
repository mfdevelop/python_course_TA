"""tempt_string = input("please insert the string :\n")
string_len = len(tempt_string)
print(string_len)"""
#############################################################
"""string1 = input("enter 1 string :\n")
string2 = input("enter 2 string :\n")
last_char_1 = string1[-1]
last_char_2 = string2[-1]
final_string = f"{string2[:-1]}{last_char_1} {string1[:-1]}{last_char_2}"
print(final_string)"""
##############################################################
"""in1 = int(input())
in2 = int(input())
in3 = int(input())
delta = (in2**2)-(4*in1*in3)
if in1 == in2 == 0:
  print('IMPOSSIBLE')
else:
  if delta > 0:
    x1 = (-in2-delta**(1/2))/2*in1
    x2 = (-in2+delta**(1/2))/2*in1
    print(int(x1))
    print(int(x2))
  if delta == 0:
    x = (-in2)/(2*in1)
    print(int(x))
  if delta < 0:
    print('IMPOSSIBLE')"""
######################################################
"""a = int(input())
b = int(input())
c = int(input())
temp1 = None
temp2 = None
MAX = None
if a > b:
    if a > c:
        MAX = a
        temp2 = b
        temp1 = c
    else:
        MAX = c
        temp2 = b
        temp1 = a
else:
    if b > c:
        MAX = b
        temp2 = a
        temp1 = c
    else:
        MAX = c
        temp2 = b
        temp1 = a

if MAX ** 2 == temp2 ** 2 + temp1 ** 2:
    print("YES")
else:
    print("NO")"""
