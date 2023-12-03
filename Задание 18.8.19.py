
price = 0
age = []
amount_t = int(input('Введите количество билетов: '))

print('Введите возраст каждого посетителя через enter:')
for i in range(amount_t):
    age.append(int(input()))
    if age[i] < 18:
        price += 0
    elif age[i] >= 18 and age[i] < 25:
        price += 990
    else:
        price += 1390
if amount_t > 3:
    price = price - price * 0.1
print('Сумма к оплате: ', int(price), ' руб.')