# a = "11"
# b = "1"
a = "1010"
b = "1011"
value = ""
final = ""
carry = "0"
i = len(a) - 1
j = len(b) - 1
index=min(i,j)
print(index)
while i >= 0 or j>=0:
    if i >= 0 and j >= 0:
        value = str((int(a[i]) ^ int(b[j])) ^ int(carry))
        carry=str(int(a[i]) & int(b[j]) | int(a[i]) & int(carry) | int(b[j]) & int(carry))
    elif i >= 0:
        value = str(int(a[i]) ^ int(carry))
        carry = str(int(a[i]) & int(carry))

    elif j >= 0:
        value = str(int(b[j]) ^ int(carry))
        carry = str(int(b[j]) & int(carry))
        print("carry 3", carry)
        print("val 3", value)
    final = value + final

    i = i - 1
    j=j-1
if carry!="0":
    final = carry + final



