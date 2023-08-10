def write_laptop_info(laptops):
    with open('laptops.txt', 'w') as file:
        for laptop in laptops:
            laptop_info = [laptop['name'], laptop['brand'], f'${laptop["price"]}', str(laptop['quantity']), laptop['processor'], laptop['graphic_card']]
            file.write(', '.join(laptop_info) + '\n')
