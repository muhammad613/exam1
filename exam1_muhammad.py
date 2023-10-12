cities = []
with open("cities.txt", 'r') as file:
    for i in file:
        city = i.strip().lower()
        cities.append(city)
# print(cities)

while True:
    city1 = input("Введите название города: ").strip().lower()
    none_city = None
    if city1 == 'stop':
        print('Программа остановалена...')
        break
    for city in cities:
        if city.startswith(city1[-1]):
            none_city = city
            break
    if none_city:
        if city1 not in cities:
            print('Такого города нет...')
            continue
        print(f"Следующий город: {none_city}")
        cities.remove(city1)
        city1 = none_city
    else:
        print("Такого города нет...")
