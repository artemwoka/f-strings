product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))

total_cost = quantity * price

print(f"Продукт: {product_name}, Кількість: {quantity}, Вартість: {total_cost}грн")

# Обчислення загальної суми продажу за день, тиждень, місяць, рік
days_in_week = 7
days_in_month = 30
days_in_year = 365

total_day = total_cost
total_week = total_cost * days_in_week
total_month = total_cost * days_in_month
total_year = total_cost * days_in_year

print(f"Сума продажу за день: {total_day}грн")
print(f"Сума продажу за тиждень: {total_week}грн")
print(f"Сума продажу за місяць: {total_month}грн")
print(f"Сума продажу за рік: {total_year}грн")