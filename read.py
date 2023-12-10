"""
read_laptops_from_file: Reads laptop details from the file "laptop.txt" 
and stores them in a dictionary called laptops_data.
"""
# Function to read laptops from a file and store them in a dictionary
def read_laptops_from_file():
    laptops_data = {}
    try:
        file = open('laptop.txt')
        for line in file:
            # Extract laptop details from each line in the file
            name, brand, price, available, ram, processor, gpu = line.strip().split(', ')
            # Store laptop details in the laptops_data dictionary
            laptops_data[name] = {'brand': brand, 'price': float(price.strip('$')), 'ram': ram, 'processor': processor, 'gpu': gpu, 'available': int(available)}
    except FileNotFoundError:
        # Handle the case when the file is not found
        print("File not found.")
    except Exception as e:
        # Handle other exceptions that may occur while reading the file
        print(f"An error occurred: {e}")
    else:
        # Close the file if it was successfully read
        file.close()
        # Return the laptops_data dictionary
        return laptops_data
    
'''
display_laptops: Displays the list of laptops and their specifications in a 
formatted table. The laptops details are obtained from the laptops_data dictionary.
'''

# Function to display the list of laptops in a formatted table
def display_laptops(laptops_data):
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("|                                Available Laptops in Stock                                                      |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("|  Laptop Name                  |   Brand   |  Price ($) |  Available |  RAM (GB)  |     Processor     |       GPU        |")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for name, details in laptops_data.items():
        brand = details["brand"]
        price = details["price"]
        available = details["available"]
        ram = details["ram"]
        processor = details["processor"]
        gpu = details["gpu"]
        print(f"| {name:<28} | {brand:<9} | ${price:>8.1f} | {available:>10} | {ram:<9} | {processor:<17} | {gpu:<15} |")
    print("-----------------------------------------------------------------------------------------------------------------------")



# Read laptops data from the file and store it in the laptops_data dictionary
laptops_data = read_laptops_from_file()

