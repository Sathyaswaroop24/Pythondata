print("Order of execution in exception")
print("------ With print ------")
def x():
    try:
        print(1)
    except:
        print(2)
    else:
        print(3)
    finally:
        print(4)
    
x()

print("------ With return ------")
def y():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4
    
print(y())