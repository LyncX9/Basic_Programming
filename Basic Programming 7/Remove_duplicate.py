number = [1, 2, 3, 4, 2, 3, 5, 6, 1]

for i in range(len(number)-1, 0, -1):
    if number[i] in number[:i]:
        del number[i]

print(number)