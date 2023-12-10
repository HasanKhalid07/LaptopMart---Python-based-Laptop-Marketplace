"""
This module implements the Hasan Laptop Store Management System, designed for the 
admin (owner) of the laptop store. The system provides various functionalities 
such as viewing all laptops available, purchasing new laptops, selling laptops, 
and quitting the program. The program is user-friendly, with a menu-based interface 
that guides the admin through different actions.
"""

print("---------------------------------------------------------------------")
print("\nWelcome, Admin! You are using Hasan Laptop Store Management System.")
print("---------------------------------------------------------------------")
print("How can we assist you today? Are you looking to buy or sell a laptop?")

#The display_menu() function displays a well-formatted menu with options for the admin to choose from.
def display_menu():
    """ """
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                       Hasan Laptop Store                      ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║    Option   ║             Menu Selection                      ║")
    print("╠═════════════╬═════════════════════════════════════════════════╣")
    print("║      1      ║             View all laptops                    ║")
    print("║      2      ║             Purchase a laptop                   ║")
    print("║      3      ║             Sell a laptop                       ║")
    print("║      4      ║             Quit                                ║")
    print("╚═════════════╩═════════════════════════════════════════════════╝")


while True:
    # Keep the options flowing! Display the menu for Admin to navigate the laptop store smoothly.
    display_menu()

    try:
        # Prompt the user to enter their preference and handle the input
        preference = int(input("Enter your preference (1-4): "))

        if preference == 1:
            # Option 1 allows the admin to view all laptops available in the store. 
            # It uses the display_laptops() function from the read module to show the laptop details to the admin.
            from read import display_laptops, laptops_data
            # Display all laptops
            display_laptops(laptops_data)
            
        elif preference == 2:
            # Option 2 allows the admin to purchase new laptops and 
            # generates a purchase receipt using the purchase_laptops_receipt() function from the write module.
            from write import purchase_laptops_receipt
            purchase_laptops_receipt()

        elif preference == 3:
            # Option 3 allows the admin to sell laptops and generates 
            # a sales receipt using the sell_laptops_receipt() function from the write module.
            from write import sell_laptops_receipt
            sell_laptops_receipt()

        elif preference == 4:
            #Option 4 is used to quit the program gracefully, displaying a farewell message to the admin.
            print("\nThank you for using Hasan Laptop Store Management System!")
            print("We hope you had a great experience managing your store.")
            print("Please come back whenever you need to manage your laptop store.\n")
            break
            
        else:
            # The program handles invalid inputs and prompts the admin to enter a valid option. 
            print("Invalid preference! Please select a preference from 1 to 4, and let the adventure continue.")
    except ValueError:
        #  # It also addresses any invalid input exceptions that may occur during the program's execution.
        print("Invalid input detected. To navigate this realm, choose a preference from 1 to 4 and continue the journey.")
    