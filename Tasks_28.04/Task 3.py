numbers = input().split()
heights = [int(num) for num in numbers]
max_height = max(heights)

for i in range(max_height, 0, -1):
    row = ""
    for height in heights:
        if height >= i:
            row += "* "
        else:
            row += "  "
    print(row)

print("-"*(2*len(heights)+1))

labels = ""
for i in range(len(heights)):
    labels += str(i+1) + " "
print(labels)
