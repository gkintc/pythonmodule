# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd

csv_to_read='https://raw.githubusercontent.com/gkintc/pythonmodule/main/dataproc_results.csv'

# Initialize the lists for X and Y
data = pd.read_csv(csv_to_read)

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Elapsed time for different tests")
plt.xlabel("Test")
plt.ylabel("Elapsed Time")

# Show the plot
plt.show()
