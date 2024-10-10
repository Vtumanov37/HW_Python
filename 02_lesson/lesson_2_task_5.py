def month_to_season(month):
    if month in (1, 2, 12):
        return ("Зима")
    elif month in (3, 4, 5):
        return ("Весна")
    elif month in (6, 7, 8):
        return ("Лето")
    elif month in (9, 10, 11):
        return ("Осень")
    else:
        return ("Неверно указан номер месяца")


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Введите целое число")
