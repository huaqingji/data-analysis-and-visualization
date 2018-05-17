## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt

true_avengers = avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

def f(row):
    num = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for column in columns:
        death = row[column]
        if death == 'NaN' or death == 'NO':
            continue
        elif death == 'YES':
            num += 1
    return num

true_avengers['Deaths'] = true_avengers.apply(f, axis=1)

## 6. Verifying Years Since Joining ##

correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)