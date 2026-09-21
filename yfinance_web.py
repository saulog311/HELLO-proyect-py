import yfinance as yf
import matplotlib.pyplot as plt

# Solicitud de datos al usuario #
ticker = input(['Ingrese el símbolo de la acción: '])
yf.download(ticker)


# Solicitud de datos al usuario de fecha de inicio y fin #

dt_start = input('Ingrese la fecha de inicio (yyyy-mm-dd): ') 
dt_end = input('Ingrese la fecha de fin (yyyy-mm-dd): ')
data = yf.Ticker(ticker)
table = data.history(start=dt_start, end=dt_end)

#valores de cierre de la acción min, max, mean #
close_table = table.Close
maximum = round(close_table.max(), 2)
minimum = round(close_table.min(), 2)
value_mean = round(close_table.mean(), 2)

print(f'El valor máximo de {ticker} es: {maximum}', end=' | ')
print(f'El valor mínimo de {ticker} es: {minimum}', end=' | ')
print(f'El valor promedio de {ticker} es: {value_mean}', '\n')
print(table)

#visualización de la acción en un gráfico #
close_table = table.Close

grafic = close_table.plot()
plt.show()