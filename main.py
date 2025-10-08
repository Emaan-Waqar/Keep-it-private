# Write a program to create a class with following variables and methods - 
# 1. Private variable named privateVar that contains an integer value 
# 2. Create a private function privMeth that prints a message 
# 3. Create a function hello that prints the value of privateVar 
# 4. Create an object for the class and call all the functions.

class Main:
    def __init__(self,privateVar):
        self.__privateVar=privateVar
    def __privMath(self):
        print("Hello")
    def Hello(self):
        self.__privMath()
        print(self.__privateVar)   
obj=Main(10)
obj.Hello()
                  