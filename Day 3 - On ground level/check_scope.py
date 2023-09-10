def add(x,y):
    z=x+y
    print('add() executed under the scope: ', __name__)
    return z

x=input('Enter the first number to add: ')
y=input('Enter the secode number to add: ')
result = add(int(x),int(y))
print(x, '+', y,'=', result)
print('Code executed under the scope: ', __name__)