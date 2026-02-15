class Employee:
    def __init__(self, name, salary):#this type of starting and ending with two _ called dunder method 
                                      # <_init_> a function called constructor which always called first
                                      #after creating a object
        # These are instance variables
        self.name = name
        self.salary = salary
    #defining a another function to greet all employee
    @staticmethod #we use it when we no need to take any data from object to run that function
                  #so we just use @staticmethod to know the function that
                  #this is a static function

    def greet():
        print(f"Welcome to our company,hope togather we will build a great empire")
#creating a object
emp1=Employee("arghya",10000000)
print(emp1.name,emp1.salary)
print(emp1.greet())
emp2=Employee()