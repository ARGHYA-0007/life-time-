try:
    a=int(input("enter a number"))


except Exception as e:
    print(e)


# this finally statement will run everytime don't matter that try or except 
# but que is that if we dont use finally and exclude that statement from try and 
# except then also that statement will run but this will help in class
# when their are return statement in try or except,cause even after return statement
# finally statement will run
finally:
    print("this statement will run when try is successfull, and code not enter in Exception")
def hell():
    try:
        a=int(input("enter a number"))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    
    finally:
        print("this statement will run when try is successfull, and code not enter in Exception")
hell()