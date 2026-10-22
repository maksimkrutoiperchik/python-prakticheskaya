<<<<<<< HEAD
# ne  slovartovarov ura
dictproducts = [
    {"id": 0, 
    "name": "мышь", 
    "category": "управления", 
    "price": 2000, 
    "quantity": 30},
    {"id": 1, 
    "name": "клавиатура", 
    "category": "управления", 
    "price": 7000, 
    "quantity": 10},
    {"id": 2, 
    "name": "монитор", 
    "category": "не управления", 
    "price": 20000, 
    "quantity": 3},
    {"id": 3, 
    "name": "наушники", 
    "category": "не управления", 
    "price": 1000, 
    "quantity": 300},
    {"id": 4, 
    "name": "веб-камера", 
    "category": "не управления", 
    "price": 4000, 
    "quantity": 35},
    {"id": 5, 
    "name": "микрофон", 
    "category": "не управления", 
    "price": 100, 
    "quantity": 5000},
    {"id": 6, 
    "name": "usb-флешка", 
    "category": "управления", 
    "price": 300, 
    "quantity": 340},
    {"id": 7, 
    "name": "колонки", 
    "category": "не управления", 
    "price": 3500, 
    "quantity": 0},
]




def print_product(item):
    """печатает строку с инфой о товаре"""
    print(f"id {item['id']}  название {item['name']}  категория {item['category']} "
          f" цена {item['price']} руб  кол-во {item['quantity']}")


def total_cost(products):
    """считает общую стоимость всех товаров"""
    total = 0
    for item in products:
        total += item['price'] * item['quantity']
    return total


def find_by_id(item_id):
    """ищет товары по их индексу (ID)"""
    for item in dictproducts:
        if item['id'] == item_id:
            return item
    return None


def input_int(prompt):
    """целое число, а если нет то будет ничего"""
    text = input(prompt).strip()
    try:
        return int(text)
    except ValueError:
        return None

def show_products(products=None):
    """выводит список и их общую стоимость, если нет аргумента выведет весь аргумент"""
    if products is None:
        products = dictproducts
    if not products:
        print("список пуст")
        return
    for item in products:
        print_product(item)
    print(f"общая стоимость товаров {total_cost(products)} рублей")



def find_product():
    """поиск по названию"""
    search = input("введите название товара (или его часть) ").strip().lower()
    found = []
    for item in dictproducts:
        if search in item['name'].lower():
            found.append(item)
    if found:
        for item in found:
            print_product(item)
    else:
        print("нет таких товаров!!!!😭😭😭")




def get_categories():
    """уникальные  категории (извините за двойной пробел он будет часто наверное я не знаю я не уверен)"""
    categories = set()
    for item in dictproducts:
        categories.add(item['category'])
    return categories


def show_by_category():
    """выводит товары выбранной категории"""
    print("доступные категори", ", ".join(sorted(get_categories())))
    category = input("введите название категории ").strip().lower()
    found = []
    for item in dictproducts:
        if item['category'].lower() == category:
            found.append(item)
    if found:
        for item in found:
            print_product(item)
    else:
        print("в этой категории нет товаров!!!!😭😭😭😭")


# ===================== ЗАДАНИЕ 4. Остатки на складе =====================
def check_stock():
    """разделяет товары на остатки"""
    out_of_stock = []
    low_stock = []
    enough_stock = []
    for item in dictproducts:
        if item['quantity'] == 0:
            out_of_stock.append(item)
        elif item['quantity'] < 5:
            low_stock.append(item)
        else:
            enough_stock.append(item)

    groups = [
        ("товаров нет на складе", out_of_stock),
        ("товаров меньше 5-ти штук", low_stock),
        ("товаров 5-ти штук  и больше", enough_stock),
    ]
    for title, group in groups:
        print(f"\n{title}:")
        if group:
            for item in group:
                print(f"  {item['name']} — {item['quantity']} шт.")
        else:
            print("  (нет)")




def restock_product():
    """увеличивает остаток товара на складе"""
    item_id = input_int("введите индекс (ID) товара: ")
    if item_id is None:
        print("ошибка id должен быть целым числом")
        return
    item = find_by_id(item_id)
    if item is None:
        print("ошибка товара с таким id не существует")
        return
    amount = input_int("сколько штук добавить ")
    if amount is None or amount <= 0:
        print("ошибка количество должно быть положительным целым числом")
        return
    item['quantity'] += amount
    print("склад пополнен обновлённая информация")
    print_product(item)



def sell_product():
    """продаёт товар со склада и выводит стоимость покупки"""
    item_id = input_int("введите id товара ")
    if item_id is None:
        print("ошибка: id должен быть целым числом")
        return
    item = find_by_id(item_id)
    if item is None:
        print("ошибка: товара с таким id не существует")
        return
    amount = input_int("сколько единиц продать ")
    if amount is None or amount <= 0:
        print("ошибка количество должно быть положительным целым числом")
        return
    if item['quantity'] < amount:
        print(f"ошибка недостаточно товара на складе {item['quantity']} штук")
        return
    item['quantity'] -= amount
    print(f"продано {item['name']} — {amount} шт Стоимость покупки {item['price'] * amount} рублей")




def show_statistics():
    """формирует отчёт по ассортименту"""
    if not dictproducts:
        print("ничего  нет")
        return

    total_units = 0
    price_sum = 0
    units_by_category = {}
    for item in dictproducts:
        total_units += item['quantity']
        price_sum += item['price']
        category = item['category']
        units_by_category[category] = units_by_category.get(category, 0) + item['quantity']

    most_expensive = max(dictproducts, key=lambda x: x['price'])
    cheapest = min(dictproducts, key=lambda x: x['price'])
    top_category = max(units_by_category, key=units_by_category.get)
    average_price = price_sum / len(dictproducts)

    print(f"различных товаров в ассортименте: {len(dictproducts)}")
    print(f"всего единиц на складе: {total_units}")
    print(f"общая стоимость товаров: {total_cost(dictproducts)} рублей")
    print(f"самый дорогой товар: {most_expensive['name']} ({most_expensive['price']} рублей)")
    print(f"самый дешёвый товар: {cheapest['name']} ({cheapest['price']} рублей)")
    print(f"категория с наибольшим количеством единиц: {top_category} ({units_by_category[top_category]} штук)")
    print(f"средняя цена одного товара: {average_price:.2f} руб")



def sort_products():
    """копия сортированного ассортимента"""
    print("1. по цене (по возрастанию)")
    print("2. по цене (по убыванию)")
    print("3. по названию (по алфавиту)")
    print("4. по количеству на складе (по возрастанию)")
    choice = input("выберите вариант сортировки: ").strip()

    if choice == "1":
        result = sorted(dictproducts, key=lambda x: x['price'])
    elif choice == "2":
        result = sorted(dictproducts, key=lambda x: x['price'], reverse=True)
    elif choice == "3":
        result = sorted(dictproducts, key=lambda x: x['name'])
    elif choice == "4":
        result = sorted(dictproducts, key=lambda x: x['quantity'])
    else:
        print("ошибка: неизвестный вариант сортировки!!!!😭😭😭😭")
        return
    show_products(result)


def main():
    while True:
        print("\n------- меню -----")
        print("1. показать все товары")
        print("2. найти товар по названию")
        print("3. показать товары выбранной категории")
        print("4. проверить остатки на складе")
        print("5. пополнить склад")
        print("6. продать товар")
        print("7. показать статистику")
        print("8. отсортировать товары")
        print("9. завершить работу программы")
        choice = input("выберите пункт меню: ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            find_product()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            check_stock()
        elif choice == "5":
            restock_product()
        elif choice == "6":
            sell_product()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            sort_products()
        elif choice == "9":
            print("работа программы завершена!!!")
            break
        else:
            print("ошибка: неизвестный пункт меню, попробуйте ещё раз.")


































# энтер залип









main()
