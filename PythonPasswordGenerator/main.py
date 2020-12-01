import string
import random


s1 = string.ascii_lowercase
# print(s1)
s2 = string.ascii_uppercase
# print(s2)
s3 = string.digits
# print(s3)
s4 = string.punctuation
# print(s4)


try:
    plen = int(input("Enter password length\n"))
except:
    print("You have entered a wrong input.")
else:
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)


    # Method_one
    print("Your password using Method_one is: ", end="")
    random.shuffle(s)
    print("".join(s[0:plen]))
    

    # Method_Two
    print("Your password using Method_two is: ", end="")
    print("".join(random.sample(s, plen)))
