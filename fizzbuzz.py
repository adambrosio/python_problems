for x in range(0, 101):
    if x % 5 == 0 and x % 3 == 0:
        print('FizzBuzz')
        continue
    elif x % 3 == 0:
        print('Fizz')
        continue
    elif x % 5 == 0:
        print('Buzz')
        continue
    else:
        print(x)