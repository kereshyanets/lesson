proceeds = int(input('введите выручку компании: '))
costs = int(input('введите издержки компании: '))
if proceeds <= costs:
        print('компания не получила прибыль')
else:
    people = int(input('введите количество сотрудников: '))
    profit = proceeds - costs
    people_profit = profit / people
    print ('прибыль на одного сотрудника равна:', (f'{people_profit:.2}'))