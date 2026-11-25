from data import get_games, get_shopping_list


temperatures = [12, 15, 18, 14, 11]

print("Temperaturer:", temperatures)
print("Antal temperaturer:", len(temperatures))


cities = ["Göteborg", "Malmö", "Stockholm", "Uppsala", "Lund"]

print("Mina städer:", cities)
print("Antal städer:", len(cities))


print("Första staden:", cities[0])
print("Tredje staden:", cities[2])
print("Sista staden:", cities[-1])


cities[1] = "Örebro"

print("Städer efter ändringen:", cities)


games = get_games()

print("Mina favoritspel:", games)
print("Antal spel:", len(games))


numbers = [10, 20, 30]

print("Från början:", numbers)

numbers.append(40)
print("Efter append:", numbers)

numbers.insert(1, 15)
print("Efter insert:", numbers)

print("Antal tal:", len(numbers))


numbers[1] = 15

print("Efter att jag ändrat ett värde:", numbers)
print("Antal tal efter ändringen:", len(numbers))


shopping_list = get_shopping_list()

print("Min inköpslista:", shopping_list)
print("Antal varor:", len(shopping_list))