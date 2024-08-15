import csv

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def main():
    try:
        # Prompt for mileage
        mileage = int(input("Enter the mileage (positive and non-zero integer): "))

        # Validate mileage
        if mileage <= 0:
            print("Mileage must be a positive, non-zero integer.")
            return

    except ValueError:
        print("Please enter a valid integer.")
        return


    # Read theta values from CSV
    # automatically closes the file when done
    with open('../data/theta.csv', mode='r') as file:
        reader = csv.reader(file)
        theta0, theta1 = next(reader)
        theta0, theta1 = float(theta0), float(theta1)

    # Calculate and print estimated price
    price = estimate_price(mileage, theta0, theta1)
    if (price >=0):
        print("The estimated price is: {}".format(round(price)))
        print("This would be different from the actual price, as the model is averaging the data points rather than overfitting. Overfitting would be a perfect fit to the data points, but would not be able to predict new data points accurately. (BONUS_1)")
    else:
        print("The model is not calibrated to give a positive valuation based on the mileage provided, please try with a mileage in range.")
#so I can run this as standalone, or just import the estimate_price function and use in 2_linear_regression.py
if __name__ == "__main__":
    main()
