import pandas as pd
import numpy as np

pd.set_option('display.width', 3000)

# read csv document 
# only show first 5 and last 5 
print("Printing cars")
car = pd.read_csv("Car.csv")
print(car)
print("")

# show first 3 and last 3
print("First and last 3 rows")
top = car.head(3)
print(top)
bottom = car.tail(3)
print(bottom)
print("")

# skip rows 
print("Read csv by skipping rows")
car2 = pd.read_csv("Car.csv", skiprows=lambda x: x%2!=0)
print(car2)
print("")

# usecols & nrows 
print("Read csv by selecting rows cols using nrows and usecols")
car2 = pd.read_csv("Car.csv", usecols=['company', 'body-style'], nrows=10)
print(car2)
print("")

# read using multiple column name or column index
print("Multiple column names")
car2 = pd.read_csv("Car.csv", index_col=['company', 'body-style'])
# same as index_col=[0, 1]
print(car2)
print("")

# print data type 
print("Car price data type")
print(car['price'].dtypes)
print("")

# change data type 
car['price'].replace(np.nan, 0, inplace=True)
car['price'] = car['price'].astype('int')
print("Car price now of type int")
print(car['price'])
print("")

# print highest and lowest car price with the corresponding columns 
print("highest and lowest car price with the corresponding columns")
highest = car[['company', 'price']][car.price==car['price'].max()]
print(highest)
highest2 = car[['horsepower', 'price']][car.price==car['price'].max()]
print(highest2)
lowest = car[['company', 'price']][car.price==car['price'].min()]
print(lowest)
lowest2 = car[['engine-type', 'price']][car.price==car['price'].min()]
print(lowest2)
print("")

# grouping and classification 
print("Car grouping 1 by company")
cargroup = car.groupby('company') # classify cars into company names 
print(cargroup) # only shows this is a groupby object 
toy = cargroup.get_group('toyota') # get a particular company's car 
print(toy)

print("Car grouping 2 by body-style")
bsgroup = car.groupby('body-style')
hb = bsgroup.get_group('hatchback')
print(hb)
print("")

# Combining both 3 and 4, group and max 
# findingthe max price of each company
print("Maximum price of car from each company")
cargroup = car.groupby('company')
price = cargroup['price'].max()
print(price)
print("")

# group and find the average value 
# finding the average mileage of each company 
print("Finding average mileage of each company")
cargroup = car.groupby('company')
avrg = cargroup['average-mileage'].mean()
print(avrg)
print("")

# counting the total 
print("Total cars produced from each company")
ctr = car['company'].value_counts();
print(ctr)
print("")

print("Total cars for each different body style")
ctr2 = car['body-style'].value_counts()
print(ctr2)
print("")

# sort by price 
print("Sort by price")
car.sort_values(by=['price'], ascending=True, inplace=True) # ascending
print(car)
car.sort_values(by=['price'], ascending=False, inplace=True) # descending
print(car)
print("")

# correlate
print("Correlate")
df = pd.read_csv('Car.csv')
df2 = df.corr()
print(df2)
print("")
