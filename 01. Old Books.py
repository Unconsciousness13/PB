book = input()
books_count = 0
IsFound = False
books_names = input()
while books_names != "No More Books":
    if books_names == book:
        IsFound = True
        print(f"You checked {books_count} books and found it.")
        break
    books_count += 1
    books_names = input()
else:
    print (f"The book you search is not here!")
    print(f"You checked {books_count} books.")

