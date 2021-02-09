def fibonacci():
    fib = [1, 1]
    i = 0
    userInput = int(input('enter: '))
    if userInput == 1:
        return '[1]'
    else:
        while i != userInput - 2:
            add = fib[-1] + fib[-2]
            fib.append(add)
            i += 1
    return fib


print(fibonacci())
