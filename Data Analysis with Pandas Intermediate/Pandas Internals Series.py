
## 1. Data Structures ##

import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango.head(2)

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')

series_film = fandango['FILM']
print(series_film.iloc[:5])

series_rt = fandango['RottenTomatoes']
print(series_film.iloc[:5])

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = Series(rt_scores , index=film_names)


## 4. Integer Index Preservation ##

fiveten = series_custom[5:11]

print(fiveten)

## 5. Reindexing ##

original_index = series_custom.index
sorted_by_index = series_custom.reindex(sorted(original_index))

## 6. Sorting ##

sc2 = series_custom.sort_index()
print(sc2[:10])

sc3 = series_custom.sort_values()
print(sc3[:10])

## 7. Transforming Columns With Vectorized Operations ##

series_normalized = series_custom / 20

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75

both_criteria = series_custom[(series_custom > 50)&(series_custom < 75)]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

rt_mean = (rt_critics + rt_users) / 2