def spam():
    global eggs
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
