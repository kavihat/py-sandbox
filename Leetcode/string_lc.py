# string1 = 'aabaab'
# # set_string=set(string1)
# # substring=''.join(set_string)
# # print(substring)
# c_full = ''
# c_chk = ''
# c_rep = ''
# for i in range(len(string1)):
#     c_full = c_full + string1[i]
#     c_chk = c_chk + string1[i]
#     if c_chk == c_rep:
#         c_chk = ''
#     elif c_chk in c_rep:
#         continue
#     else:
#         c_chk = ''
#         c_rep = c_full
#
# print(c_full)
# print(c_rep)
#
# print(c_rep != c_full)

# else:
#     c_rep=''

# len_sub_string=len(c_rep)
# print(len_sub_string)
# var=len(string1)/len_sub_string
# print(var)
# if (len(string1)/len_sub_string).is_integer() and len(string1)!=1 and string1.count(c_rep)==var:
#     print(True)
# else:
#     print(False)




string1 = "abacababacab"
c_full = ''
c_chk = ''
c_rep = ''
for c in string1:
    c_full += c
    c_chk += c
    if c_chk == c_rep:
        c_chk = ''
    elif c_rep.startswith(c_chk):
        pass
    else:
        c_chk = ''
        c_rep = c_full

    print(c_full)
    print(c_rep)
    print(c_chk)
    print('____________')

print(c_rep != c_full and c_chk == '')