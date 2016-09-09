def collatz(number):
    if number == 1:
        print(number)
    elif number % 2 == 0:
        number = number // 2
        print(number)
        collatz(number) 
    else:
        number = 3 * number + 1
        print(number)
        collatz(number)
    
print('Enter a number.')
collatz(int(input()))
print('Done.')

        
