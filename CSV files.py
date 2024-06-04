# Как мы все знаем айтишники любят путешествовать, а география студентов Urban'а очень большая.
# Все они были в разных городах и странах, но посетить осталось ещё не мало. Выпускники уже  планируют, куда поедут после окончания курсов отдохнуть.
# Нужно помочь им определить, кто в каких городах был и в какие города они хотят поехать.
# Определите, какие города можно выбрать для путешествия, при условии, что никто из потока в них никогда не был.
#
# Напишите функцию write_holiday_cities(first_letter), которая:
# Принимает параметром первую букву имени человека - first_letter.
# Функция должна:
# Получить данные из travel_notes.csv и записать в holiday.csv:
# В каких городах студенты с именем на first_letter уже были.
# Какие города студенты с именем на first_letter хотят посетить.
# В каких городах студенты с именем на first_letter ещё не были.
# Какой первый город эти студенты посетят (в алфавитном порядке)

import csv

def write_holiday_cities(first_letter):
    cities = []

    with open('travel-notes.csv', 'r', newline='') as cvs_file:
        reader = csv.reader(cvs_file)
        for row in reader:
            cities.append(row)

    filtred_data = []
    for n in cities:
        name, visited_cities, wanted_cities = n[0], n[1].split(';'), n[2].split(';')
        if name.startswith(first_letter):
            filtred_data.append((name, visited_cities, wanted_cities))
            print(name, visited_cities, wanted_cities)

    # for data in filtred_data:
    #     print(f"Name: {data[0]}")
    #     print(f"Visited Cities: {', '.join(data[1])}")
    #     print(f"Wanted Cities: {', '.join(data[2])}")
    #     print()  # Пустая строка для разделения записей

    all_visited_cities = set()
    all_wanted_cities = set()
    for _, visited_cities, wanted_cities in filtred_data:
        all_visited_cities.update(visited_cities)
        all_wanted_cities.update(wanted_cities)
    never_visited_cities = all_wanted_cities - all_visited_cities
    first_city_to_visit = sorted(never_visited_cities)[0] if never_visited_cities else 'None'
    with open('holiday.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for name, visited_cities, wanted_cities in filtred_data:
            writer.writerow([name, visited_cities, wanted_cities, list(never_visited_cities), first_city_to_visit])

write_holiday_cities('L')


