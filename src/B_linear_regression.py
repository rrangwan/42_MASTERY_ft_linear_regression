# the use of python numpy.polyfit is considered cheating
# learning resource: https://learn.wqu.edu :
# 0201-quantitative-methods/lessons/0201-1-1-linear-regression/


#Task 1: Prepare Date
# 1.1 Import the necessary libraries
# pandas is used for data manipulation

import csv
import pandas as pd


# import the function from A_estimate_price.py to estimate price
from A_estimate_price import estimate_price


# Normalize data
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]


# also will later need to denormalize the data
def unnormalized_thetas(theta0, theta1, min_mileage, max_mileage, min_price, max_price):
    unnormalized_theta1 = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    unnormalized_theta0 = theta0 * (max_price - min_price) + min_price - unnormalized_theta1 * min_mileage
    return unnormalized_theta0, unnormalized_theta1


#This is the regression model (did not use library to do it for me)
def gradient_descent(mileage, price, filename):
    m = len(mileage)  # Number of data points
    learning_rate = 0.01 # hyperparameter
    iterations = 10000  # Number of iterations to run gradient descent

    #Read theta values from CSV and use for training
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        theta0, theta1 = next(reader)
        theta0, theta1 = float(theta0), float(theta1)

    # theta0, theta1 = 0.0, 0.0

    for _ in range(iterations):
        tmp_theta0 = 0.0
        tmp_theta1 = 0.0

        # Calculate the gradient for theta0 and theta1
        for i in range(m):
            error = estimate_price(mileage[i], theta0, theta1) - price[i]
            tmp_theta0 += error
            tmp_theta1 += error * mileage[i]

        # Update theta0 and theta1
        theta0 -= learning_rate * (tmp_theta0 / m)
        theta1 -= learning_rate * (tmp_theta1 / m)

        # Write updated theta values back to CSV in each iteration
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([theta0, theta1])

# need to denormalize the data
def unnormalized_thetas(theta0, theta1, min_mileage, max_mileage, min_price, max_price):
    unnormalized_theta1 = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    unnormalized_theta0 = theta0 * (max_price - min_price) + min_price - unnormalized_theta1 * min_mileage
    return unnormalized_theta0, unnormalized_theta1


# Now to update the theta values as unnormalized
def unnormalize_thetas(min_mileage, max_mileage, min_price, max_price, filename):
    # Read theta values from CSV
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        theta0, theta1 = next(reader)
        theta0, theta1 = float(theta0), float(theta1)

    theta0_n, theta1_n = unnormalized_thetas(theta0, theta1, min_mileage, max_mileage, min_price, max_price)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([theta0_n, theta1_n])



#finally save the predicted price to a csv file called data2.csv
def create_predicted_prices(filename1, filename2, filename3):

    mileage_data = []
    predicted_prices = []

    # Read theta values from CSV
    with open(filename2, mode='r') as file:
        reader = csv.reader(file)
        theta0, theta1 = next(reader)
        theta0, theta1 = float(theta0), float(theta1)

    with open(filename1, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mileage = float(row['km'])
            predicted_price = estimate_price(mileage, theta0, theta1)
            mileage_data.append(mileage)
            predicted_prices.append(predicted_price)

    with open(filename3, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['mileage', 'predicted_price'])  # Write the header
        for mileage, predicted_price in zip(mileage_data, predicted_prices):
            writer.writerow([mileage, predicted_price])


def main():
    # Explore the data
    # Read the data from the csv file
    data = pd.read_csv('../data/data.csv')
    data.dropna(inplace=True)
    mileage = data['km']
    price = data['price']
    filename1 = '../data/data.csv'
    filename2 = '../data/theta.csv'
    filename3 = '../data/data2.csv'

    
    # start with thetas set to 0

    with open(filename2, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([0, 0])

    #save values before normalizing
    min_price = min(price)
    max_price = max(price)
    min_mileage = min(mileage)
    max_mileage = max(mileage)

    
    # Normalize data to avoid overflows (large numbers)

    mileage = normalize(mileage)
    price = normalize(price)

    gradient_descent(mileage, price, filename2)

    unnormalize_thetas(min_mileage, max_mileage, min_price, max_price, filename2)

    create_predicted_prices(filename1, filename2, filename3)

if __name__ == "__main__":
    main()
