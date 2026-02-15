a=int(input("enter your number which need to be devided"))
b=int(input("enter your divider"))
if b==0:
    # here we are raising our custom error so that user dont enter 0 and recognize their fault
    raise ZeroDivisionError("this program will not allow to devide by zero pls retry with new devider")
else:
    print("value: ",a/b)