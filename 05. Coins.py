sum = float(input())
sum *= 100
coin_counter = 0
coin_counter += sum // 200
sum = sum % 200
coin_counter += sum // 100
sum = sum % 100
coin_counter += sum // 50
sum = sum % 50
coin_counter += sum // 20
sum = sum % 20
coin_counter += sum // 10
sum = sum % 10
coin_counter += sum // 5
sum = sum % 5
coin_counter += sum // 2
sum = sum % 2
if sum == 1:
    coin_counter += 1
print(int(coin_counter))
