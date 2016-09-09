korrok = [ 'I ', 'serve ', 'none ', 'but ', 'Korrok ']

for k in range(1, 101):
    global korrok
    if k % 7 == 0:
        print(korrok[0])
        del korrok[0]
        if len(korrok) == 0:
            break
    else:
        print(k)
    
    
