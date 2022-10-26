n = 18
g = 0
while(True):
    print('Enter the number : ')
    a = int(input())

    if(g==5):
        print('Sorry, game over')
        break

    elif(a>n):
        g=g+1
        print('The number is greater and you have ',5-g,' try left')
        
        continue

    elif(a<n):
        g=g+1
        print('The number is smaller and you have ',5-g,' try left')
        
        continue

    else:
        print('This is the perfect number')
        break


