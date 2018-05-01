
## 3. Read in a CSV file ##

import pandas as pd

food_info = pd.read_csv('food_info.csv')
print(type(food_info))

## 4. Exploring the DataFrame ##

first_twenty = food_info.head(20)

## 7. Selecting a row ##

hundredth_row = food_info.loc[99]
print(hundredth_row)

## 8. Data types ##

print(food_info.dtypes)

## 9. Selecting multiple rows ##

rows = food_info.shape[0]

last_rows = food_info.loc[rows-5:rows]

## 10. Selecting individual columns ##

saturated_fat = food_info['FA_Sat_(g)']
cholesterol = food_info['Cholestrl_(mg)']

## 11. Selecting multiple columns by name ##

selenium_thiamin = food_info[['Selenium_(mcg)','Thiamin_(mg)']]

## 12. Practice ##

col_names = list(food_info.columns)
gram_columns = [name for name in col_names if name.endswith('(g)')]
gram_df = food_info[gram_columns]
gram_df.head(3)