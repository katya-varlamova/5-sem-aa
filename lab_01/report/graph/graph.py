import matplotlib.pyplot as plt
x = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
y1 = [2.00, 1.10, 0.60, 1.20, 1.30, 1.60, 1.80, 2.00, 2.30, 2.70]
y2 = [0.40, 3.20, 14.40, 74.50, 405.10, 2202.90, 11775.30, 80139.50, 381142.50, 2107292.80]
y3 = [0.80, 2.50, 13.50, 70.70, 384.50, 2126.70, 11715.60, 64279.70, 357540.30, 1980920.40]
y4 = [5.80, 1.50, 2.10, 2.50, 2.80, 3.30, 4.30, 4.70, 4.90, 5.90]
# Построение графика
plt.xlabel("Суммарный размер строк")
plt.ylabel("Время выполнения")
plt.plot(x, y1, label = "Нерекурсивный")
plt.plot(x, y2, label = "Дам.-Лев.")
plt.plot(x, y3, label = "Рекурсивный")
plt.plot(x, y4, label = "Рек. с кэшем")
plt.axis([6, 24, 0, 2107293])
plt.legend()
plt.show()
