import datetime
import write

def generate_invoice(laptop, customer_name, transaction_type, transaction_amount, shipping_cost=0):
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    laptop_name_cleaned = laptop['name'].replace(":", "_").replace("/", "_").replace("\\", "_")
    customer_name_cleaned = customer_name.replace(":", "_").replace("/", "_").replace("\\", "_")
    invoice_name = f"{customer_name_cleaned}_{laptop_name_cleaned}_{date_time}.txt"
    with open(invoice_name, 'w') as file:
        file.write(f"Transaction Type: {transaction_type}\n")
        file.write(f"Laptop Name: {laptop['name']}\n")
        file.write(f"Laptop Brand: {laptop['brand']}\n")
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"Transaction Date and Time: {date_time}\n")
        file.write(f"Transaction Amount: {transaction_amount}\n")
        if transaction_type == 'Sale':
            file.write(f"Shipping Cost: ${shipping_cost}\n")
            file.write(f"Total Amount: ${transaction_amount + shipping_cost}\n")
        elif transaction_type == 'Order':
            vat = transaction_amount * 0.13
            file.write(f"VAT Amount: ${vat}\n")
            file.write(f"Gross Amount: ${transaction_amount + vat}\n")

def sell_laptop(laptops, laptop_name, customer_name, shipping_cost=0):
    for laptop in laptops:
        if laptop['name'] == laptop_name:
            if laptop['quantity'] > 0:
                laptop['quantity'] -= 1
                transaction_amount = laptop['price']
                generate_invoice(laptop, customer_name, 'Sale', transaction_amount, shipping_cost)
                print(f"{laptop_name} sold to {customer_name}.")
                write.write_laptop_info(laptops)
                return
            else:
                print(f"{laptop_name} is out of stock.")
                return
    print(f"{laptop_name} not found.")

def order_laptop(laptops, laptop_name, distributor_name):
    for laptop in laptops:
        if laptop['name'] == laptop_name:
            laptop['quantity'] += 1
            transaction_amount = laptop['price']
            generate_invoice(laptop, distributor_name, 'Order', transaction_amount)
            print(f"{laptop_name} ordered from {distributor_name}.")
            write.write_laptop_info(laptops)
            return
    print(f"{laptop_name} not found.")

def add_laptop(laptops):
    name = input("Enter laptop name: ")
    brand = input("Enter laptop brand: ")
    
    while True:
        price_input = input("Enter laptop price: ")
        try:
            price = float(price_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the price.")

    while True:
        quantity_input = input("Enter laptop quantity: ")
        try:
            quantity = int(quantity_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer value for the quantity.")

    processor = input("Enter laptop processor: ")
    graphic_card = input("Enter laptop graphic card: ")

    laptop = {
        'name': name,
        'brand': brand,
        'price': price,
        'quantity': quantity,
        'processor': processor,
        'graphic_card': graphic_card
    }

    laptops.append(laptop)
    write.write_laptop_info(laptops)
    print(f"{name} added to inventory.")
