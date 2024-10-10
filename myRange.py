def myRange(*args):
    myList = []
    isTrue = True
    myType =  "s"
    for i in args:
        try:
            int(i)
        except ValueError:
            isTrue = False
            myType = "String"
            break
    for i in args:
        if(type(i) == float):
            isTrue = False
            myType = "Float"
    if(isTrue):
        if(len(args) == 1):
            for i in range(args[0]):
                myList.append(i)
        elif(len(args) == 2):
            for i in range(args[0] , args[1]):
                myList.append(i)
        elif(len(args) == 3):
            for i in range(args[0] , args[1] , args[2]):
                myList.append(i)
        return tuple(myList)
    else:
        return(f"You Entered Wrong Type of Variable {myType}")

print(myRange(2.5))
