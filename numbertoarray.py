def digitize(n):
    return [int(i) for i in str(n)[::-1]]

def digitize_with_map(n):
    return list(map(int, str(n)[::-1]))


print(digitize(1231023),digitize_with_map(12332344))