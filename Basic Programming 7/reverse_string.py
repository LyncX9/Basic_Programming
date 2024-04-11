name = input("input your name:")
Reversed_name = ""

for i in range(len(name)-1,-1,-1,):
    Reversed_name += name[i]

print("your reversed name is:", Reversed_name)