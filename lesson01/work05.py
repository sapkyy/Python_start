# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
profit = int(input('Выручка '))
costs = int(input('Издержки '))
earnings = profit - costs
if profit > costs:
    print('Хорошо поработали!')
    print(f"Рентабельность: {round((profit / costs), 2)}")
    people = int(input('Сколько человек в штате? '))
    print(f"Прибыль на одного работника: {round((earnings / people), 2)}")
else:
    print('Поработали так себе...')
