# this is a program that says hello and asks for my name.

print('Hello world!')

print('What is your name?')     #ask for their name

myName = input()

print('it is good to meet you, ' + myName)

print('the length of your name is:')

print(len(myName))

print('What is your age?')      #ask for their age

myAge = input()

print()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
