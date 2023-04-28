all_items = []
unique_items = set()
repeat_items = set()
while True:
    s = input().strip()
    if s == "-1":
        for item in all_items:
            if item not in repeat_items:
                if item not in unique_items:
                    unique_items.add(item)
                else:
                    unique_items.remove(item)
                    repeat_items.add(item)
        all_items = []
        continue
    if s == "":
        break
    all_items.append(int(s))
for item in all_items:
    if item not in repeat_items:
        if item not in unique_items:
            unique_items.add(item)
        else:
            unique_items.remove(item)
            repeat_items.add(item)
print(" ".join(str(i) for i in unique_items))
