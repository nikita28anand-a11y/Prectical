name = input("enter name:")
if name.isupper():
    print("uppercase")
elif name.islower():
    print("lowercase")
elif name.isdigit():
    print("digit")
else: 
    print("special character")

