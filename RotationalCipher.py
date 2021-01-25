


def rotationalCipher(input, rotation_factor):
    # Write your code here
    output = ""
    for i in range(len(input)):
        if input[i].isalnum():
            if ord(input[i]) >= ord('a') and ord(input[i]) <= ord('z'):
                output+= chr((((ord(input[i]) - ord('a')) + rotation_factor) % 26) + ord('a'))
                print(output,input[i])
            elif ord(input[i]) >= ord('A') and ord(input[i]) <= ord('Z'):
                output+=chr((((ord(input[i]) - ord('A')) + rotation_factor) % 26) + ord('A'))
                print(output,input[i])
            else:
                output+= chr((((ord(input[i]) - ord('0')) + rotation_factor) % 10) + ord('0'))


        else:
            output += input[i]
    return output



print(rotationalCipher("Zebra-493",3))


