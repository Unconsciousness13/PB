tabs_opened = int(input())
salary = int(input())
for text in range(tabs_opened):
    web_text = input()
    if web_text == "Facebook":
        salary -= 150
    elif web_text == "Instagram":
        salary -= 100
    elif web_text == "Reddit":
        salary -= 50
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
