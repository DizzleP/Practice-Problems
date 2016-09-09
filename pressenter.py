name = ''
password = ''
hint = 'The password is a fish.'
guess = 0

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break
    else:
        print('Wrong! Please try again.')
        guess = guess + 1
        if guess >= 3:
            print(hint)
        continue
print('Access granted.')
