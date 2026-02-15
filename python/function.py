# function without any arguement
def letsstart():
    print("hello guys how are you chai pee lo")

letsstart() 


# function with arguement
def goodday(name,ending):
    print(f"very good day,{name}")
    print(ending)
goodday("arghya","chal be haoa ane day")


# another way to call function
def goodday(name,ending):
    print(f"very good day,{name}")
    print(ending)
    return "done"
a=goodday("arghya","chal be haoa ane day")
print(a)


# default argument in function 
def goodday(name,ending="thank you"):
    print(f"very good day,{name}")
    print(ending)
goodday("arghya","chal be haoa ane day")
goodday("aniruddha")#here is no ending argument i have given
                    #so in default output will be |very good day,aniruddha
                    #thank you|