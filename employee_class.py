#Module file for employee class
class Employee:
    def __init__(self):
        #Get name and number from user for attributes.
        self.__name = str(input("Please enter the employee's name:"))
        self.__number = int(input("Please enter the employee's number:"))
    
    #Setters and Getters for attributes.
    def set_name(name):
        self.__name = name

    def get_name():
        return self.__name

    def set_number(number):
        self.__number = int(number)

    def get_number():
        return self.__number
