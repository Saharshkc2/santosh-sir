import read
import operations

# Main loop
laptops = read.read_laptop_info()
while True:
    print('''
    1. Sell laptop
    2. Order laptop
    3. Add laptop
    4. Quit
    ''')
    choice = input("Enter your choice: ")
    if choice == '1':
        laptop_name = input("Enter laptop name: ")
        customer_name = input("Enter customer name: ")
        shipping_cost = float(input("Enter shipping cost (default is 0): ") or 0)
        operations.sell_laptop(laptops, laptop_name, customer_name, shipping_cost)
    elif choice == '2':
        laptop_name = input("Enter laptop name: ")
        distributor_name = input("Enter distributor name: ")
        operations.order_laptop(laptops, laptop_name, distributor_name)
    elif choice == '3':
        operations.add_laptop(laptops)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
