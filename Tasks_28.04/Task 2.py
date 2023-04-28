m = int(input())
fridge = set()
for i in range(m):
    fridge.add(input().strip())

n = int(input())
recipes = []
for i in range(n):
    name = input().strip()
    k = int(input())
    ingredients = set()
    for j in range(k):
        ingredients.add(input().strip())
    recipes.append((name, ingredients))

can_cook = []
for name, ingredients in recipes:
    if ingredients.issubset(fridge):
        can_cook.append(name)

for name in can_cook:
    print(name)
