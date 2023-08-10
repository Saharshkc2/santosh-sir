def read_laptop_info():
    laptops = []
    with open('laptops.txt', 'r') as file:
        for line in file:
            laptop_info = line.strip().split(', ')
            laptop = {
                'name': laptop_info[0],
                'brand': laptop_info[1],
                'price': float(laptop_info[2].replace('$', '')),
                'quantity': int(laptop_info[3]),
                'processor': laptop_info[4],
                'graphic_card': laptop_info[5]
            }
            laptops.append(laptop)
    return laptops
