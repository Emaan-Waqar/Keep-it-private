# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:
    def __init__(self,max_price,):
        self.__max_price=max_price
    def sell(self):
        print(f"the slling price is {self.__max_price}")  
    def setmaxprice(self, maxPrice):
        self.__max_price= maxPrice          
    def get_max_price(self):
        return self.__max_price
    def set_max_price(self, new_price):
        if new_price < self.__max_price or new_price > self.__max_price:
            self.__max_price= new_price
        else:
            print("Invalid")    

obj=Computer(1500)
print(obj.get_max_price())
obj.set_max_price(2000)
print(obj.get_max_price())