'''recursion means when a fuction call himself then its called recursion
   example:
   fact(1)=1
   fact(2)=2X1
   fact(3)=3X2X1
   fact(4)=4X3X2X1
   .
   .
   .
   fact(n)=nXfact(n-1) <here while getting the value of fact of any number we need to
                       run the exact function for the number just 1 down of that number> 
   
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number for which you want to know its factorial: "))
print(f"value: {factorial(n)}")