import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
x = [100, 200, 300, 400, 500]
y1 = [1614.33, 6333.63, 14180.2, 25329.2, 39221.8]
y2 = [1045.01, 4143.79, 9655.59, 17172.8, 25637.5]
y4 = [545.895, 2226.87, 5155.55, 9462.02, 15123.8]
y8 = [374.916, 1617.05, 3743.16, 6907.58, 10955.2]
y16 = [409.756, 1752.07, 4057.03, 7311.09, 11746.3]
y32 = [421.671, 1805.8, 4087.55, 7360.05, 11631.2]
fig, ax = plt.subplots()
# Построение графика
plt.xlabel("Размер изображения (x * x)")
plt.ylabel("Время выполнения (мс)")
plt.plot(x, y1, label = "1 поток")
plt.plot(x, y2, label = "2 потока")
plt.plot(x, y4, label = "4 потока")
plt.plot(x, y8, label = "8 потоков")
plt.plot(x, y16, label = "16 потоков")
plt.plot(x, y32, label = "32 потока")
plt.legend()
plt.show()

