
## 2. Array Comparisons ##

countries_canada = world_alcohol[:, 2] == 'Canada'

years_1984 = world_alcohol[:, 0] == '1984'

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:, 2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

## 5. Replacing Values ##

world_alcohol_is_1986 = world_alcohol[:,0] == '1986'
world_alcohol[world_alcohol_is_1986, 0] = '2014'

world_alcohol_is_wine = world_alcohol[:,3] == 'Wine'
world_alcohol[world_alcohol_is_wine, 3] = 'Grog'



## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty, 4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

# good example for numpy
canada_1986 = world_alcohol[ (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada'), :]

canada_alcohol = canada_1986[:,4].astype(float)

total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

# claculate the total assumption for certain country in 1989
totals = {}
for country in countries:
    
    consumption_country_1989  = world_alcohol[(world_alcohol[:,0] == '1989') & (world_alcohol[:,2] == country), 4]
    
    total_consumption_country_1989 = consumption_country_1989.astype(float).sum()
    
    totals[country] = total_consumption_country_1989

## 11. Finding the Country that Drinks the Most ##

# find the country with the highest total alcohol consumption
highest_value = 0
highest_key = None

for country in totals:
    if totals[country] > highest_value:
        highest_value = totals[country]
        highest_key = country

