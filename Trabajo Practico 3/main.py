import pandas as pd

hojaExcel = pd.read_excel('./TablaCapitales.xlsx')

print(hojaExcel.values)
print(hojaExcel.columns)
