#Module file for employee class
class Employee:
    def __init__(self):
        #Get name and number from user for attributes.
        self.__name = str(input("Please enter the employee's name:"))
        self.__number = int(input("Please enter the employee's number:"))
    
    #Setters and Getters for attributes.
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = int(number)

    def get_number(self):
        return self.__number
