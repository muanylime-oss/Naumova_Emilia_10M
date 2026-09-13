temperature = float(input("Введите температуру (°C):"))
print(f"Температура по Цельсию: {temperature} °C")
print(f"Температура по Фаренгейту: {temperature*9/5 + 32} °F")
print(f"Температура по Кельвину: {temperature + 273.15 + 0.000000001:.1f} K")