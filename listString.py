def andAnother(thing):
    for i in range(len(thing)):
        newSpam = ''
        newSpam += spam[i]
        if i == len(thing) - 1:
            newSpam += '.'
            print(newSpam)
        elif i < len(thing):
            newSpam += ', and '

spam = ['apples', 'bananas', 'tofu', 'cats']
andAnother(spam)

