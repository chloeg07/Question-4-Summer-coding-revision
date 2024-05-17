#Question 4
sales_persons = []
sales_values = []
def display_menu():
    print("\n*** Welcome ***")
    print("Please choose an option below: ")
    print("1. Enter sales data")
    print("2. View total sales to date")
    print("3. View maximum sale value of any staff member")
    print("4.View minimum sale of any staff member")
    print("5.View average sale value of any staff member")
    print("6. Exit")

def enter_sales_data():
    name = input("Enter the name of the sales person:  ")
    while True:
        try:
            value = float(input("Enter the value of the sale:  "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value. ")
    sales_persons.append(name)
    sales_values.append(value)
    print("Sales data entered successfully. ")

def view_total_sales():
    total_sales = sum(sales_values)
    print("Total sales to date: €{:.2f}".format(total_sales))
    
def view_max_sales():
    name = input("Enter the name of the sales person: ")
    if name in sales_persons:
        indices = [i for i, x in enumerate(sales_persons) if x ==name]
        max_sales = max(sales_values[i] for i in indices)
        print("Maximum sale value of {}: €{:.2f}".format(name, max_sale))
    else:
        print("Sales person not found.")
        
def view_min_sale():
    name = input("Enter the name of the sales person: ")
    if name in sales_persons:
        indices = [i for i, x in enumerate(sales_persons) if x == name]
        min_sale = min(sales_values[i] for i in indices)
        print("Minimum sale value of {}: €{:.2f}".format(name, min_sale))
    else:
        print("Sales person not found.")
        
def view_avg_sale():
    name = input("Enter the name of the sales person: ")
    if name in sales_persons:
        indices = [i for i, x in enumerate(sales_persons) if x == name]
        avg_sale = sum(sales_values[i] for i in indices) / len(indices)
        print("Average sale value of {}: €{:.2f}".format(name, avg_sale))
    else:
        print("Sales person not found. ")
    
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue
    
    if choice == 1:
        enter_sales_data()
    elif choice == 2:
        view_total_sales()
    elif choice == 3:
        view_max_sale()
    elif choice == 4:
        view_min_sale()
    elif choice == 5:
        view_avg_sale()
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice.Please enter a number between 1 and 6")
    
        
    
            