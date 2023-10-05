import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from numpy import median

# Load data from a CSV file into a Pandas DataFrame
dataset = pd.read_csv("emgraw.csv")

x = pd.DataFrame(dataset.iloc[:,:-1])
y = pd.DataFrame(dataset.iloc[:,-1])
#sb.barplot(x = dataFrame["Academy"], y = dataFrame["Matches"], estimator = median)

# display
#plt.show()



