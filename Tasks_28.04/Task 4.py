stack = []

for elem in input().split():
    if elem.isdigit():
        stack.append(int(elem))
    elif elem == '!':
        stack.append(math.factorial(stack.pop()))
    elif elem == '#':
        stack.append(stack[-1])
    elif elem == '@':
        a, b, c = stack.pop(), stack.pop(), stack.pop()
        stack.extend([b, c, a])
    else:
        b, a = stack.pop(), stack.pop()
        if elem == '+':
            stack.append(a + b)
        elif elem == '-':
            stack.append(a - b)
        elif elem == '*':
            stack.append(a * b)
        elif elem == '/':
            stack.append(int(a / b))
        elif elem == '_':
            stack.append(-a)
print(stack.pop())
