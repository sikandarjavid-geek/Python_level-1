def addNum(Num1,Num2):
    if type(Num1) == type(Num2) ==  int:
        return Num1+Num2
    else:
        return "Sorry, I need Integers!"

result = addNum(2,3)
print(result)
mylist = [1,2,3,4,5,6,7,8,9,10]

evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))
