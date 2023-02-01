from random import randint, choice
import csv

NUM_MERCHANDISE = 100

if __name__ == '__main__':
    by_category = {
        'Laptop': {
            'Lenovo': (130, 2500, ['ThinkPad', 'IdeaPad', 'Legion']),
            'Apple': (250, 2500, ['MacBook Air']),
            'HP': (130, 2500, ['EliteBook', 'Pavilion', 'ProBook']),
            'ASUS': (130, 2500, ['ZenBook', 'ROG Strix', 'VivoBook']),
            'Dell': (130, 2500, ['G', 'Vostro', 'Latitude'])
        },
        'Keyboard': {
            'Asus': (3, 50, ['TUF :C:N', 'Rog :C:N']),
            'Razer': (5, 80, ['Huntsman', 'Tartarus']),
            'Logitech': (3, 60, [':C:N:N Mechanical', 'Craft Wireless']),
            'Steelseries': (3, 50, ['Apex :N']),
        },
        'Computer Mouse': {
            'Logitech': (2, 50, ['Wireless :C:N:N:N', 'Lightspeed', 'G:N:N:N']),
            'Asus': (5, 50, ['TUF :C:N', 'Rog :C:N']),
            'Razer': (2, 50, ['Orochi :C:N', 'Viper :C:N', 'Naga :C:N']),
            'Lenovo': (2, 50, ['Legion :N:N', 'Professional :C:N', 'ThinkBook :C:N'])
        },
        'Smartphones': {
            'Samsung': (40, 600, ['Galaxy :C:N:N', 'Galaxy :C:N:N Plus', 'Galaxy :C:N:N Fold', 'Galaxy :C:N Ultra']),
            'Apple': (210, 850, ['iPhone', 'iPhone Pro', 'iPhone Pro Max']),
            'Xiaomi': (40, 500, ['Redmi Note :N', 'Poco :C:C:N']),
            'Huawei': (40, 150, ['Nova :C:N'])
        }
    }


    letters = 'qwertyuiopasdfghjklzxcvbnm'
    digits = '1234567890'
    with open('tech_inventory.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['model', 'category', 'brand', 'price'])
        writer.writeheader()
        for i in range(NUM_MERCHANDISE):
            category = choice(list(by_category.keys()))
            brand = choice(list(by_category[category].keys()))
            price = randint(by_category[category][brand][0], by_category[category][brand][1]) * 100 + randint(1, 9) * 10 + choice([0, 5, 9])
            model = choice(list(by_category[category][brand][2]))
            while ':C' in model:
                model = model.replace(':C', choice(letters).upper(), 1)
            while ':N' in model:
                model = model.replace(':N', choice(digits).upper(), 1)
            writer.writerow(
                {
                    'model': model,
                    'category': category,
                    'brand': brand,
                    'price': price
                }
            )
