from mod import module
module() # here the if statement in the real mod.py file will not run cause here 
         # __name__ not equal to __main__


print(__name__)