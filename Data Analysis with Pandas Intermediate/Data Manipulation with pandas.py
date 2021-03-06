
## 1. Overview ##

import pandas as pd

food_info = pd.read_csv('food_info.csv')
col_names = food_info.columns.tolist()
print(col_names)

## 2. Transforming a Column ##

sodium_grams = food_info['Sodium_(mg)'] /  1000 
sugar_milligrams = food_info['Sugar_Tot_(g)'] * 1000

## 3. Performing Math with Multiple Columns ##

grams_of_protein_per_gram_of_water = food_info['Protein_(g)'] / food_info['Water_(g)']

milligrams_of_calcium_and_iron = food_info['Calcium_(mg)'] + food_info['Iron_(mg)']

## 4. Create a Nutritional Index ##

weighted_protein = 2 * food_info['Protein_(g)']

weighted_fat = -0.75 * food_info['Lipid_Tot_(g)']

initial_rating = weighted_protein + weighted_fat

## 5. Normalizing Columns in a Data Set ##

normalized_protein = (food_info['Protein_(g)'] - food_info['Protein_(g)'].min())/(food_info['Protein_(g)'].max() - food_info['Protein_(g)'].min())

normalized_fat = (food_info['Lipid_Tot_(g)'] - food_info['Lipid_Tot_(g)'].min())/(food_info['Lipid_Tot_(g)'].max() - food_info['Lipid_Tot_(g)'].min())

## 6. Creating a New Column ##

food_info['Normalized_Protein'] = (food_info["Protein_(g)"] - food_info["Protein_(g)"].min()) / (food_info["Protein_(g)"].max() - food_info["Protein_(g)"].min())
food_info['Normalized_Fat'] = (food_info["Lipid_Tot_(g)"] - food_info["Lipid_Tot_(g)"].min()) / (food_info["Lipid_Tot_(g)"].max() - food_info["Lipid_Tot_(g)"].min())

## 7. Create a Normalized Nutritional Index ##

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat
food_info["Norm_Nutr_Index"] = 2* food_info["Normalized_Protein"] - 0.75 * food_info["Normalized_Fat"]


## 8. Sorting a DataFrame by a Column ##

food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])


food_info.sort_values('Norm_Nutr_Index', inplace=True, ascending=False)