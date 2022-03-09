# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Alicia Y, 3.7.2022, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product (object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Alicia Y, 3.7.2022, Modified code to complete assignment 8
    """
    pass

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # 	   -- Attributes --
        try:
            self.__product_name = product_name
            self.__product_price = product_price
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    # -- Properties -
    # product_name
    @property  # DON'T USE NAME for this directive!
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # product_price
    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        if str(value).isnumeric():
            self.__product_price = float(value)  # cast to float
        else:
            raise Exception("Prices must be numbers")


# -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Alicia Y, 3.7.2022, Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Write data to a file from a list of product rows

        param file_name: (string) with name of file
        param list_of_product_objects: (list) of product objects data saved to a file
        return (bool) status of success_status

        """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
        return success_status


    # TODO: Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of product rows

        :param file_name: (string) with name of file
        :return: (list) of product rows
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows

        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Performs Input and Output tasks

    methods:
        output_menu_tasks :
        input_menu_choice :
        output_current_data (list_of_rows) :
        input_new_product :


    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Alicia Y, 3.7.2022, Modified code to complete assignment 8
    """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        """ Display a menu of choices to the user
        :return: nothing
        """

    print('''
     Menu of Options
     1) Show current data
     2) Add data
     3) Save data to a file
     4) Exit program
     ''')
    print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """

        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_data(list_of_rows: list):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """

        print("******* The current products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product():
        """ Gets product and price values to be added to the list
        :return: (Product) object with input data
        """
        try:
            UserProduct = str(input("What is the product ? - ")).strip()
            UserPrice = float(input("What is the price? - "))
            print()
            UserObj = Product(product_name=UserProduct, product_price=UserPrice)

        except Exception as e:
            print(e)
        return UserObj

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
    # Show user a menu of options
        IO.output_menu_tasks()
    # Get user's  menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.output_current_data(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_new_product())
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')


