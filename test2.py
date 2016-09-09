age = input()
age = int(age)
if age == 11:
    print('Congratulations Harry, you are old enough to be a wizard!')
elif age < 11:
    print('Harry, you are not old enough to be a wizard yet!')
elif age >= 12 and age <= 100:
    print('You are at a good age to be a wizard Harry!')
elif age > 101:
    print('You are a bit too old to be a wizard now, Harry!')
print('Done') 


print('Are you Ganesh?')
identity = input()

if identity == 'yes':
    print('Are you graceful?')
    graceQuantity = input()
    if graceQuantity == 'no':
        print('You are not Ganesh! Ganesh is graceful!')
    else:
        print('Welcome, Ganesh.')
else:
    print('Then move along.')

print('Done.') 
            
