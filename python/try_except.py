# with out try
a=int(input("enter a number"))
print("this will not run if user enter invalid input")
# here if user enter any thing except a integer number the program will show error and 
# will stop and will not exicute next 


try:
    a=int(input("enter a number"))
except Exception as e:
    print(e)
print("but this statement will run even after entering invalid input")
# But here when we use try and except this will not stop the program even if the user enter
# invalid number 