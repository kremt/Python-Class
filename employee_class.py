#Module file for employee class
class Employee:
    def __init__(self):
        #Get name and number from user for attributes.
        self.__name = set_name()
        self.__number = set_number()
    
    #Setters and Getters for attributes.
    def set_name(self):
        self.__name = input("Please enter the employee's name:")

    def get_name(self):
        return self.__name

    def set_number(self):
        self.__number = input("Please enter the employee's number:")

    def get_number(self):
        return self.__number
