sum = float(input())
coin_counter = 0
while sum != 0:
    sum = int(sum * 100)
    if sum // 200:
        sum = sum % 200
        coin_counter += 1
    if sum // 100:
        sum = sum % 100
        coin_counter += 1
    if sum // 50:
        sum = sum % 50
        coin_counter += 1
    if sum // 20:
        sum = sum % 20
        coin_counter += 1
    if sum // 10:
        sum = sum % 10
        coin_counter += 1
    if sum // 5:
        sum = sum % 5
        coin_counter += 1
    if sum // 2:
        sum = sum % 2
        coin_counter += 1

    break
print(int(coin_counter))
