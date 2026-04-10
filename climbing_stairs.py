def climbing_stairs(n: int):
    first, second = 1, 1

    for i in range(n - 1):
        print(i)
        temp = first
        first = first + second
        second = temp 
    return first
print(climbing_stairs(5))