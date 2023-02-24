#=====importing libraries===========
import os
os.chdir("C:\\Users\\nazza\\Documents\\Nazmus\\HyperionDev\\Capstone 4")        #Use to change working directory (so tasks.txt and user.txt files are correctly detected)
#print (os.getcwd())            #Uncomment to check your working directory


#========The beginning of the class==========
class Shoe:
    #initialiser
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
    #get cost of object
    def get_cost(self):
        return(self.cost)
    #get quantity of object
    def get_quantity(self):
        return(int(self.quantity))
    #get string representation of object
    def __str__(self):
        string_shoe = f'''
Country = \t{self.country}
Code = \t{self.code}
Product = \t{self.product}
Cost = \t{self.cost}
Quantity = \t{self.quantity}
'''
        return(string_shoe)
        


#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    with open ("inventory.txt", "r") as f:              #open file
        for line_index, line in enumerate (f):
            if (line_index > 0):                        #read all lines apart from the first
                shoe = line.strip().split(",")          #remove whitespace and split into list
                #create shoe object if line has correct number of variables
                try:
                    new_shoe = Shoe(shoe[0],shoe[1],shoe[2],shoe[3],shoe[4])
                    shoe_list.append(new_shoe)  #add to shoe list
                except IndexError as error:
                    print(error)


def capture_shoes():
    #get input from user
    country = input("Please enter the country of the shoes: ")
    code = input("Please enter the code of the shoes: ")
    product = input("Please enter the product of the shoes: ")
    cost = input("Please enter the cost of the shoes: ")
    quantity = input("Please enter the number of sheos: ")
    #create shoe object
    new_shoe = Shoe(country,code,product,cost, quantity)
    shoe_list.append(new_shoe)  #add to shoe list
    

def view_all():
    for shoe in shoe_list:      #iterate through shoe list and call '__str__' function on each shoe
        print (shoe.__str__())  


def re_stock():
    lowest_shoe = shoe_list[0]      #set default for shoe object with lowest quantity
    for shoe_index, shoe in enumerate (shoe_list):      #loop through shoe list
        if (shoe.get_quantity() < lowest_shoe.get_quantity()):      #get quantity of current shoe object and lowest shoe object and compare
            lowest_shoe = shoe          #update lowest shoe to current shoe if lower quantity
            lowest_shoe_index = shoe_index      #update index of lowest shoe
    #print lowest shoe
    print(f"The shoe with the lowest quantity is: {lowest_shoe.__str__()}")
    add_quantity = int(input("What quantity of shoe would you like to add to this shoe? ")) #get quantity to add
    lowest_shoe.quantity += add_quantity    #add quantity to shoe attribute
    shoe_list[lowest_shoe_index] = lowest_shoe  #replace with updated object in shoe list


def seach_shoe():
    shoe_code = input("What is the code of the shoe you would like to search for? ")    #get input to search for
    for shoe in shoe_list:
        if shoe.code == shoe_code:  #check code of each shoe in shoe list
            searched_shoe = shoe    #if match then save shoe to 'searched_shoe'
        
    print(searched_shoe.__str__())  #print string representation of 'searched_shoe'


def value_per_item():
    for shoe in shoe_list:
        value = shoe.quantity*shoe.cost     #work out value of each shoe in shoe list and print the string representation
        print(shoe.__str__())
        print (f"Value = {value}")  #print the value after the string representation 


def highest_qty():
    highest_shoe = shoe_list[0]         #default shoe for highest quantity
    for shoe_index, shoe in enumerate (shoe_list):      #compare quantity with current highest shoe and each shoe in list
        if (shoe.get_quantity() > highest_shoe.get_quantity()):
            highest_shoe = shoe #update highest shoe if quantity is higher
    #print string representation of highest qunatity shoe and that the shoe is for sale
    print(highest_shoe.__str__())
    print("This shoe is for sale!")

#==========Main Menu=============
while True: 
    #get user choice in main menu
    menu = input('''Select one of the following Options below:      
r - Read shoes data
a - Add a shoe
va - View all shoes
rs - re-stock shoe
s- search shoe
v - see stock value of each shoe
hq - see shoe with highest stock amount
e - Exit
: ''').lower()      

    #call the relevant method depending on user selection
    if menu == 'r':
        read_shoes_data()
    elif menu == 'a':
        capture_shoes()
    elif menu == 'va':
        view_all()        
    elif menu == 'rs':
        re_stock()
    elif menu == 's':
        seach_shoe()
    elif menu == "v":
        value_per_item()
    elif menu == "hq":
        highest_qty()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")

