number = float(input())
in_currency = str(input())
out_currency = str(input())
score = 0
if in_currency == "mm":
    if out_currency == "m":
        score = number / 1000

    elif out_currency == "cm":
        score = number / 10


elif in_currency == "cm":
    if out_currency == "mm":
        score = number * 10

    elif out_currency == "m":
        score = number / 100

elif in_currency == "m":
    if out_currency == "mm":
        score = number * 1000

    elif out_currency == "cm":
        score = number * 100
print (f"{score:.3f}")