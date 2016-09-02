for i in range(1,101):
    fizz = list(range(3,101,3))
    buzz = list(range(5,101,5))
    string = ''
    if i not in fizz and i not in buzz:
        print(i)
    if i in fizz:
        string += 'Fizz'
    if i in buzz:
        string += 'Buzz'
    if string != '':
        print(string)
