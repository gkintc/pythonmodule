

import pandas as pd
import plotly.express as px

csv_to_read='https://raw.githubusercontent.com/gkintc/pythonmodule/main/CET_HPB.csv'

csv_to_read_2='https://raw.githubusercontent.com/gkintc/pythonmodule/main/applecsv.csv'

df1 = pd.read_csv(csv_to_read)

df2 = pd.read_csv(csv_to_read_2)

# print(df.head(-5))

applechart = px.line(df2, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')

resultschart = px.line(df1, x = 'SYSTEM', y = 'BENCH0', title='SYSTEM VS BENCH0')

# applechart.show()

resultschart.show()



