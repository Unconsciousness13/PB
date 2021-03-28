width_in_meters = float(input())
height_in_meters = float(input())
height_in_meters > 3 < width_in_meters < 100
width_in_meters *= 100
height_in_meters *= 100
corridor = 100
width_in_meters = width_in_meters - corridor
work_place_height = 70
work_place_width = 120
desk = 70 * 40
chair_place = 70 * 80
desk_chair = desk + chair_place
door = 160 // 120
department = 160 // 70
places_width = int(width_in_meters / work_place_width)
places_height = int(height_in_meters / work_place_height)
total_places = places_height * places_width - door - department
print(total_places)

# heigth = float(input())  # Получаваме като вход височината (дължината) на залата
# width = float(input())  # Получаваме като вход ширината на залата
# width = width * 100 - 100  # Пресмятаме ширината на залата в сантиметри и вадимразмера на коридора
# heigth = heigth * 100  # Пресмятаме височината (дължината) на залата в сантиметри
# rows = heigth // 120  # Пресмятаме с целочислено деление колко реда с работни места биха се събрали
# columns = width // 70  # Пресмятаме с целочислено деление колко колони с работни места биха се събрали
# free_places = int(rows * columns)  # Пресмятаме точния брой работни места, които биха се събрали и преобразуваме в int
# free_places -= 1 + 2  # Изваждаме работните места, които се заемат от вратата и катедрата
# print(free_places)  # Принтираме резултата