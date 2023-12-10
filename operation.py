'''
The "operation.py" module serves as a crucial component of the Hasan Laptop Store Management System, 
empowering the admin to perform two primary functions: selling laptops to customers and purchasing 
new laptops directly from the manufacturer.
'''

from read import laptops_data

# The "display_laptops_data(laptops_data)" function facilitates the admin in showcasing the list 
# of available laptops in stock to potential customers.
def display_laptops_data(laptops_data):
    print("Laptops in stock: Explore and choose!")
    for i, name in enumerate(laptops_data.keys()):
        print(f"{i+1}. {name}")

# Empty global dictionary to store sold laptops' data during laptop sales transactions.
sold_laptops_data = {}

'''
 "sell_laptops_data(laptops_data)" function is called in write.py module, the admin can seamlessly navigate 
 the process of selling laptops. The module allows the admin to select a laptop for sale, verify its 
 availability, display detailed specifications, and execute the transaction.
'''
def sell_laptops_to_customer(laptops_data):
    
    print("Welcome to the Laptop Selling Interface!")
    print("You are now selling laptops to the customers.")
    print(f"Please follow the prompts below to complete the transaction.\n\n")

    while True:
        try:
            # Display available laptops for sale
            display_laptops_data(laptops_data)
            # Prompt user to choose a laptop to sell
            laptop_choice = int(input("Please enter the laptop's serial number you want to sell: "))
            
            if 1 <= laptop_choice <= len(laptops_data):
                ''' 
                Converting the keys of the 'laptops_data' dictionary into a list to access the laptop 
                name based on the user's choice of laptop serial number.
                '''
                laptop_name = list(laptops_data.keys())[laptop_choice - 1]
                laptop = laptops_data[laptop_name]

                # Check if the selected laptop is available for sale
                # If the selected laptop is not available (available quantity is 0), the loop restarts, prompting the user to choose another laptop.
                if laptop['available'] == 0:
                    print(f"Sorry, {laptop_name} laptop is not available. Please choose another laptop.")
                    continue
                # Display the dazzling specifications of the selected laptop
                print(f"\nPresenting the dazzling specifications of the {laptop_name} laptop:")
                print("=" * 60)
                print(f"{'Brand:':<15} {laptop['brand']}")
                print(f"{'Price:':<15} ${laptop['price']}")
                print(f"{'RAM:':<15} {laptop['ram']} GB")
                print(f"{'Processor:':<15} {laptop['processor']}")
                print(f"{'GPU:':<15} {laptop['gpu']}")
                print(f"{'Availability:':<15} {laptop['available']}")
                print("=" * 60)
                

                while True:
                    try:
                        # # Get the quantity of laptops the customer wants to sell.
                        sell_quantity = int(input(f"How many {laptop_name} would you like to sell? "))
                        if sell_quantity <= 0:
                            print("Invalid input. Please enter a quantity greater than 0.")
                            continue
                        # And check if it is available in stock.
                        if sell_quantity <= laptop['available']:
                            # If available, update sold_laptops_data.
                            sold_laptops_data[laptop_name] = {'price': laptop['price'], 'quantity': sell_quantity}
                            '''                   
                            After successful transactions, the module automatically updates the laptops' availability 
                            in the inventory to ensure accurate tracking of stock.
                            '''
                            laptops_data[laptop_name]['available'] -= sell_quantity
                            with open("laptop.txt", "w") as file:
                                for name, details in laptops_data.items():
                                    file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                            print(f"Sold {sell_quantity} {laptop_name} for ${sell_quantity * laptop['price']}.")
                            break
                        else:
                            print(f"Sorry, only {laptop['available']} {laptop_name} are available.")
                            print("Please ask the customer to:")
                            print("- Lower their desired quantity.")
                            print("- Choose another laptop with available quantity.")
                            '''
                            If the desired quantity of a particular laptop is unavailable, the admin is guided to either lower the customer's 
                            desired quantity or suggest another laptop with available stock.
                            '''
                            action_choice = input("Enter 'l'for lower quantity or 'a' for another laptop: ").lower()
                            if action_choice == 'l':
                                continue
                            elif action_choice == 'a':
                                break
                            else:
                                print("Invalid input. Please enter 'lower' or 'another'.")

                    except ValueError:
                        print("Invalid input. Please enter a number.")

                while True:
                    '''
                    Ask the customer if they want to sell another laptop. If 'y', break the loop.
                     If 'n', return from the function. Otherwise, prompt for input again.
                    '''
                    continue_choice = input("Would you like to sell another laptop? (y/n) ")
                    if continue_choice.lower() == 'n':
                        return
                    elif continue_choice.lower() == 'y':
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(laptops_data)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")





#empty dictionary to store purchased laptops_data
purchased_laptops_data = {}
'''
The purchase_from_manufacturer(laptops_data) function empowers the admin to restock the store by 
purchasing new laptops directly from the manufacturer.
'''
def purchase_from_manufacturer(laptops_data):

    ## Display the welcome message for the laptop purchasing interface
    print("Welcome to Hasan Laptop Store Management System!")
    print("You are now in the laptop purchasing interface.")
    print("Follow the prompts below to purchase laptops from manufacturer.")

    while True:
        # Display the menu options
        print("\nWhat would you like to do?")
        print("  1. Update the stock of laptops you already have")
        print("  2. Purchase new latest laptops")
        print("  3. Exit from purchasing")
        # Prompt the user to enter their choice and handle the input
        action = input("Enter your choice (1/2/3): ")

        if action == "1":
            # Display the list of available laptops
            display_laptops_data(laptops_data)
            try:
                # Prompt the user to choose a laptop and update its stock
                laptop_choice = int(input("Please choose the serial number of the laptop you want to update: "))
                laptop_name = list(laptops_data.keys())[laptop_choice - 1]
                laptop = laptops_data[laptop_name]
                # Display the dazzling specifications of the selected laptop
                print(f"\nPresenting the dazzling specifications of the {laptop_name} laptop:")
                print("=" * 60)
                print(f"{'Brand:':<15} {laptop['brand']}")
                print(f"{'Price:':<15} ${laptop['price']}")
                print(f"{'Availability:':<15} {laptop['available']}")
                print("=" * 60)
                additional_stock = int(input(f"Enter the additional quantity of '{laptop_name}' you want to add: "))
                if additional_stock <= 0:
                    print("Invalid input. Please enter a quantity greater than 0.")
                    continue
                current_stock = laptops_data[laptop_name]['available']
                laptops_data[laptop_name]['available'] = current_stock + additional_stock
                laptop = laptops_data[laptop_name]
                # Update the laptop.txt file with the new stock
                with open("laptop.txt", "w") as file:
                    for name, details in laptops_data.items():
                        file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                file.close()
                # Storing the purchased laptop data in the dictionary for invoice generation
                purchased_laptops_data[laptop_name] = {'price': laptop['price'], 'quantity': additional_stock}
                print(f"\nStock of '{laptop_name}' updated successfully!")
            except ValueError:
                print("\nInvalid input. Please try again.")

        elif action == "2":
            # Get the details of the new laptop from the user
            try:
                while True:
                    laptop_name = input("Please enter the name of the new laptop: ")
                    if laptop_name.strip():
                        break
                    else:
                        print("Laptop name cannot be empty. Please try again.")

                while True:
                    laptop_brand = input("Please enter the brand of the new laptop: ")
                    if laptop_brand.strip():
                        break
                    else:
                        print("Laptop brand cannot be empty. Please try again.")

                while True:
                    try:
                        laptop_price = float(input("Please enter the price of the new laptop: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid price (e.g., 1000.0).")

                while True:
                    try:
                        laptop_ram = int(input("Please enter the RAM of the new laptop (in GB): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid RAM value (e.g., 8).")

                while True:
                    laptop_processor = input("Please enter the processor of the new laptop: ")
                    if laptop_processor.strip():
                        break
                    else:
                        print("Laptop processor cannot be empty. Please try again.")

                while True:
                    laptop_gpu = input("Please enter the GPU of the new laptop: ")
                    if laptop_gpu.strip():
                        break
                    else:
                        print("Laptop GPU cannot be empty. Please try again.")

                while True:
                    try:
                        laptop_purchased = int(input(f"Please enter the number of {laptop_name} being purchased: "))
                        if laptop_purchased > 0:
                            break
                        else:
                            print("Invalid input. The number of laptops purchased must be greater than 0.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                # Add the new laptop to the laptops_data dictionary
                laptops_data[laptop_name] = {
                    'brand': laptop_brand,
                    'price': laptop_price,
                    'ram': laptop_ram,
                    'processor': laptop_processor,
                    'gpu': laptop_gpu,
                    'available': laptop_purchased
                }
                
                # Update the laptop.txt file with the new stock
                with open("laptop.txt", "w") as file:
                    for name, details in laptops_data.items():
                        file.write(f"{name}, {details['brand']}, ${details['price']}, {details['available']}, {details['ram']}, {details['processor']}, {details['gpu']}\n")
                file.close()
                #Storing in the dictionary for invoice generation
                purchased_laptops_data[laptop_name] = {'price': laptop_price, 'quantity': laptop_purchased}
                print("\nNew laptop added to the stock successfully!")
            except ValueError:
                print("\nInvalid input. Please try again.")

        elif action == "3":
            # Quit the program
            print("\nThank you for using Hasan Laptop Store! Have a great day!")
            return
        
        else:
            print("\nInvalid input. Please choose an option from 1, 2, or 3.")
