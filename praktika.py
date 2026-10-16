slovartovarov = [ 
    {
    "id": 0,
    "name": "мышь",
    "category": "управления",
    "price": 2000,
    "quantity": 30
    },
    {
    "id": 1,
    "name": "клавиатура",
    "category": "управления",
    "price": 7000,
    "quantity": 10
    },
    {
    "id": 2,
    "name": "монитор",
    "category": "не управление",
    "price": 20000,
    "quantity": 3
    },
    {
    "id": 3,
    "name": "наушники",
    "category": "не управления",
    "price": 1000,
    "quantity": 300
    },
    {
    "id": 4,
    "name": "веб-камера",
    "category": "не управления",
    "price": 4000,
    "quantity": 35
    },
    {
    "id": 5,
    "name": "микрофон",
    "category": "не управления",
    "price": 100,
    "quantity": 5000
    },
    {
    "id": 6,
    "name": "usb-флешка",
    "category": "управления",
    "price": 300,
    "quantity": 340
    } 
]

cena_tovarov = 0

for item in slovartovarov:
    print(f"id {item['id']} название {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
    
    cena_tovarov += item['price'] * item['quantity']

print(f"общая стоимость товаров {cena_tovarov} рублей")

search = input("введите свой товар который хотите ").lower()

found = []

for item in slovartovarov:
    if search in item['name'].lower():
        found.append(item)

if found:
    for item in found:
        print(f"id {item['id']} имя {item['name']} категория {item['category']} цена {item['price']} кол-во {item['quantity']}")
else:
    print('нет таких товаров')