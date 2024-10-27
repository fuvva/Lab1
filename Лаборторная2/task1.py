money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = money_capital
month_counter = 0
while budget > (spend - salary):
    month_counter += 1
    budget -= (spend - salary)
    spend = spend * (1 + increase)


print("Количество месяцев, которое можно протянуть без долгов:", month_counter)
