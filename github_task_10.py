time = int(input("Введите количество секунд с момента старта:"))
print(f"Время с момента старта: {time} секунд.")
time_hours = time//3600
time_minutes = time%3600//60
time_seconds = time - time_hours*3600 - time_minutes*60
print(f"Форматированное время: {time_hours} ч {time_minutes} мин {time_seconds} сек.")