x: int = int(input())
if x >= 0:
    i = x
    y = 0
    while i:
        y = (y + i % 10) * 10
        i //= 10
    y //= 10
    if x == y:
        print(f'{x} is a palindrome!')
    else:
        print(f'{x} is not a palindrome!')
else:
    print(f'{x} is not a palindrome!')
