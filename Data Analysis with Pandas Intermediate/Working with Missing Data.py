
## 2. Introduction ##

import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

## 3. Finding the Missing Data ##

age_is_null = pandas.isnull(titanic_survival['age'])
age_null_true = titanic_survival['age'][age_is_null]
age_null_count = len(age_null_true)
print(age_null_count)

## 4. Whats the big deal with missing data? ##

age_is_null = pd.isnull(titanic_survival['age'])
age_not_null = titanic_survival['age'][age_is_null == False]
correct_mean_age = age_not_null.mean()

## 5. Easier Ways to Do Math ##

correct_mean_fare = titanic_survival['fare'].mean()

## 6. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}
for class_num in passenger_classes:
    fares_for_class_class = titanic_survival[titanic_survival['pclass'] == class_num]['fare']
    fares_by_class[class_num] = fares_for_class_class.mean()


## 7. Making Pivot Tables ##

import numpy as np

passenger_age = titanic_survival.pivot_table(index='pclass', values='age', aggfunc=np.mean)

print(passenger_age)



## 8. More Complex Pivot Tables ##

import numpy as np

port_stats = titanic_survival.pivot_table(index='embarked', values=['fare','survived'], aggfunc=np.sum)

print(port_stats)

## 9. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=1)

new_titanic_survival = titanic_survival.dropna(axis=0, subset =['age','sex'])

## 10. Using iloc to Access Rows by Position ##

# We have already sorted new_titanic_survival by age
first_ten_rows = new_titanic_survival.iloc[0:10]

row_position_fifth = new_titanic_survival.iloc[4]

row_index_25 = new_titanic_survival.loc[25]

## 11. Using Column Indexes ##

row_index_1100_age = new_titanic_survival.loc[1100,'age']
row_index_25_survived = new_titanic_survival.loc[25,'survived']
five_rows_three_cols = new_titanic_survival.iloc[:5,:3]


## 12. Reindexing Rows ##

titanic_reindexed = new_titanic_survival.reset_index(drop=True, inplace=False)
print(titanic_reindexed.iloc[:5,:3])

## 13. Apply Functions Over a DataFrame ##

def null_count(column):
    nulls = column[pandas.isnull(column)]
    return len(nulls)

column_null_count = titanic_survival.apply(null_count)

## 14. Applying a Function to a Row ##

def is_minor(row):
    if row['age'] < 18:
        return 'minor'
    elif row['age'] >= 18:
        return 'adult'
    elif pd.isnull(row['age']):
        return 'unknown'

age_labels = titanic_survival.apply(is_minor, axis=1)

pd.isnull(age_labels)

## 15. Calculating Survival Percentage by Age Group ##

age_group_survival = titanic_survival.pivot_table(index='age_labels', values='survived', aggfunc=np.mean)