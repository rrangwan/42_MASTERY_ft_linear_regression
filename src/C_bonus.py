# Importing the necessary libraries
# matplotlib is used for plotting the data
# pandas is used for data manipulation

import matplotlib.pyplot as plt
import pandas as pd

# Set the font to Times
plt.rcParams['font.family'] = 'Times New Roman'

# 1.2 Explore the data
# Read the data from the csv file
data = pd.read_csv('../data/data.csv')
data2 = pd.read_csv('../data/data2.csv')

data.dropna(inplace=True)
data2.dropna(inplace=True)

mileage = data['km']
price = data['price']
predicted_price = data2['predicted_price']

#bonus2: Plot Data
plt.scatter(mileage, price)
plt.xlabel('Mileage [in km]')
plt.ylabel('Price [in USD]')
plt.title('BONUS_2: Price vs Mileage of Used Cars')
plt.show()


#bonus3: Add Regression line to the plot
plt.plot(mileage, predicted_price, color="orange", label="Regression Model")
plt.scatter(x=data['km'], y=data['price'])
plt.xlabel('Mileage [in km]')
plt.ylabel('Price [in USD]')
plt.title('BONUS_3: Price vs Mileage of Used Cars with Regression Line')
plt.show()

#bonus4: Add Regression line and plot predicted Values
plt.plot(mileage, predicted_price, color="orange", label="Regression Model")
plt.scatter(x=data['km'], y=data2['predicted_price'])
plt.xlabel('Mileage [in km]')
plt.ylabel('Predicted Price [in USD]')
plt.title('BONUS-4: Predicted Price vs Mileage of Used Cars with Regression Line')
plt.show()


#bonus5: Mean Absolute Error
def mean_absolute_error(actual, predicted):
    return sum([abs(a - p) for a, p in zip(actual, predicted)]) / len(actual)

print(f"BONUS_5: The Mean Absolute Error is: {round(mean_absolute_error(price, predicted_price))}\n This is the amount the predicted price is off by (+/-) on average.")



