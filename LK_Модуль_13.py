tic = int(input('Введите количество билетов: '))
total = 0.0
fullCost = 1390
partialCost = 990
for i in range(tic):
    age = int(input('Введите возраст: '))
    if 18 <= age < 25:
        total = total + partialCost
    if age >= 25:
        total = total + fullCost
if tic > 3:
    total *= 0.9
print('Итого'+ ' ' + str(total) + ' ' + 'рублей')
