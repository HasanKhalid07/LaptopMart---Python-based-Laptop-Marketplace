import datetime

# Function to sell laptops_data and generate the invoice
def sell_laptops_receipt():
    from read import laptops_data
    from operation import sell_laptops_to_customer, sold_laptops_data
    
    # Call the operation function to sell laptops_data and populate the sold_laptops_data dictionary
    sell_laptops_to_customer(laptops_data)

    # Calculate the total price
    total_price = sum([sold_laptop['price'] * sold_laptop['quantity'] for sold_laptop in sold_laptops_data.values()])
    has_discount = input("Is there any discount? (y/n): ").lower()

    if has_discount == 'y':
        try:
            discount_percent = float(input("Enter the discount percentage: "))
            if discount_percent < 0 or discount_percent > 100:
                print("Invalid discount percentage. Please enter a value between 0 and 100.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid discount percentage.")
            return
    

        discount_amount = (total_price * discount_percent) / 100
        discounted_price = total_price - discount_amount

        print(f"The discount amount is: ${discount_amount:.2f}")
        print(f"The discounted price is: ${discounted_price:.2f}")
    elif has_discount == 'n':
        print("No discount applied.")
        discount_amount = 0
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

    name = input("Please enter the customer's name: ")
    while not name.isalpha():
        name = input("Please enter a valid name: ")

    phone_number = input("Please enter the customer's phone number: ")
    while not phone_number.isnumeric():
        phone_number = input("Please enter a valid phone number: ")

    address = input("Please enter the customer's address: ")
    while not address.replace(' ', '').isalnum():
        address = input("Please enter a valid address: ")
    
    # Ask user if they want their product shipped
    shipping_choice = input("Do you want your product shipped? (Y/N): ")

    # If the user wants the product shipped, ask for the distance and calculate the shipping price
    shipping_price = 0
    if shipping_choice.lower() == "y":
        distance = float(input("Please enter the distance from the shop to the customer's house in km: "))
        if distance > 10:
            shipping_price = 50
        elif distance > 1:
            shipping_price = 10

    now = datetime.datetime.now()
    invoice_number = f"INV_sell_{name}_{now.strftime('%Y%m%d%H%M%S')}"
    invoice_filename = f"{invoice_number}.txt"

    with open(invoice_filename, "w") as file:
        file.write("=========== Hasan Laptop Store ===========\n")
        file.write("Customer Name: " + name + "\n")
        file.write("Contact: " + phone_number + "\n")
        file.write("Date: " + str(datetime.date.today()) + "\n")
        file.write("------------------------------------------\n")
        file.write("Laptop Name    Quantity    Unit Price    Total Price\n")
        for laptop_name, sold_laptop in sold_laptops_data.items():
            file.write(f"{laptop_name:<15}{sold_laptop['quantity']:<13}${sold_laptop['price']:<14}${sold_laptop['quantity']*sold_laptop['price']:<12}\n")
        file.write("------------------------------------------\n")
        file.write(f"Net Amount: ${total_price:<30}\n")
        file.write(f"Discount: ${discount_amount:<32}\n")
        file.write(f"Shipping Charge: ${shipping_price:<25}\n")
        file.write("------------------------------------------\n")
        file.write(f"Grand Total: ${total_price - discount_amount + shipping_price:<24}\n")
        file.write("------------------------------------------\n")
        file.write("Thanks for shopping with Hasan Laptop Store!\n")
        file.write("==========================================\n")

    file.close()

    print("=========== Hasan Laptop Store ===========\n")
    print("Customer Name: " + name + "\n")
    print("Contact: " + phone_number + "\n")
    print("Date: " + str(datetime.date.today()) + "\n")
    print("------------------------------------------\n")
    print("Laptop Name    Quantity    Unit Price    Total Price\n")
    for laptop_name, sold_laptop in sold_laptops_data.items():
        print(f"{laptop_name:<15}{sold_laptop['quantity']:<13}${sold_laptop['price']:<14}${sold_laptop['quantity']*sold_laptop['price']:<12}\n")
    print("------------------------------------------\n")
    print(f"Net Amount: ${total_price:<30}\n")
    print(f"Discount: ${discount_amount:<32}\n")
    print(f"Shipping Charge: ${shipping_price:<25}\n")
    print("------------------------------------------\n")
    print(f"Grand Total: ${total_price - discount_amount + shipping_price:<24}\n")
    print("------------------------------------------\n")
    print("Thanks for shopping with Hasan Laptop Store!\n")
    print("==========================================\n\n\n")

    print(f"Invoice '{invoice_number}' generated successfully.")




# Function to purchase laptops_data and generate the invoice
def purchase_laptops_receipt():
    from read import laptops_data
    from operation import purchase_from_manufacturer, purchased_laptops_data
    
    #function called from operation
    purchase_from_manufacturer(laptops_data)

    while True:
        try:
            discount_choice = input("Is there any discount? (y/n): ").lower()
            if discount_choice == 'y':
                discount_percentage = int(input("Enter the discount percentage: "))
                break
            elif discount_choice == 'n':
                discount_percentage = 0
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter a valid discount percentage.")
    print("Please note that there is a VAT of 13% on the total amount.")

    # Calculate the total price
    total_amount = sum([purchase_laptop['price'] * purchase_laptop['quantity'] for purchase_laptop in purchased_laptops_data.values()])
    discount_amount = (discount_percentage / 100) * total_amount
    net_amount = discount_amount + total_amount
    vat_amount = 0.13 * total_amount

    distributor_name = input("Please enter the distributor's name: ")
    while not distributor_name.isalpha():
        distributor_name = input("Please enter a valid name: ")

    contact_number = input("Please enter the distributor's phone number: ")
    while not contact_number.isnumeric():
        contact_number = input("Please enter a valid phone number: ")

    distributor_address = input("Please enter the distributor's address: ")
    while not distributor_address.replace(' ', '').isalnum():
        distributor_address = input("Please enter a valid address: ")

    now = datetime.datetime.now()
    invoice_number = f"INV_PUR_{distributor_name}_{now.strftime('%Y%m%d%H%M%S')}"
    invoice_filename = f"{invoice_number}.txt"

    with open(invoice_filename, "w") as file:
        file.write("===============================================\n")
        file.write(f"{distributor_name} Laptop Store\n")
        file.write("===============================================\n")
        file.write(f"Date: {datetime.date.today()}   Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
        file.write("===============================================\n")
        file.write("Laptop Name      Quantity   Unit Price   Total Price\n")
        for laptop_name, purchase_laptop in purchased_laptops_data.items():
            file.write(f"{laptop_name:<15}{purchase_laptop['quantity']:<12}${purchase_laptop['price']:<12}${purchase_laptop['quantity']*purchase_laptop['price']:<12}\n")
        file.write("===============================================\n")
        file.write(f"Discount: ${discount_amount:<10}\n")
        file.write(f"Net Amount (after discount): ${net_amount :<10}\n")
        file.write(f"VAT: ${vat_amount:<20}\n")
        file.write("===============================================\n")
        file.write(f"Total Amount (including VAT): ${total_amount:<10}\n")
        file.write("===============================================\n")
        file.write(f"{' ':<45}{distributor_name.split()[0]}\n")
        file.write(f"{' ':<45}Distributor Signature\n")
    file.close()

    print("===============================================\n")
    print(f"{distributor_name} Laptop Store\n")
    print("===============================================\n")
    print(f"Date: {datetime.date.today()}   Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
    print("===============================================\n")
    print("Laptop Name      Quantity   Unit Price   Total Price\n")
    for laptop_name, purchase_laptop in purchased_laptops_data.items():
        print(f"{laptop_name:<15}{purchase_laptop['quantity']:<12}${purchase_laptop['price']:<12}${purchase_laptop['quantity']*purchase_laptop['price']:<12}\n")
    print("===============================================\n")
    print(f"Discount: ${discount_amount:<10}\n")
    print(f"Net Amount (after discount): ${net_amount :<10}\n")
    print(f"VAT: ${vat_amount:<20}\n")
    print("===============================================\n")
    print(f"Total Amount (including VAT): ${total_amount:<10}\n")
    print("===============================================\n")
    print(f"{' ':<45}{distributor_name.split()[0]}\n")
    print(f"{' ':<45}Distributor Signature\n")


    print(f"Invoice '{invoice_number}' generated successfully.")

