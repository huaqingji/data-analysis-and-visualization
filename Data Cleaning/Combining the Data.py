## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"][data["class_size"]['GRADE ']=='09-12'] 

class_size = class_size[class_size['PROGRAM TYPE']=='GEN ED'] 

class_size.head(5)

## 5. Computing Average Class Sizes ##

import numpy as np

class_size = class_size.groupby('DBN').agg(np.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
data["class_size"].head(3)

## 7. Condensing the Demographics Data Set ##

data["demographics"] = data["demographics"][data["demographics"]['schoolyear'] == 20112012]

data["demographics"].head(3)

## 9. Condensing the Graduation Data Set ##

data['graduation'] = data['graduation'][data['graduation']['Cohort']=='2006']

data['graduation'] = data['graduation'][data['graduation']['Demographic']=='Total Cohort']

data["graduation"].head(3)

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data['ap_2010'][col]= pd.to_numeric(data['ap_2010'][col], errors="coerce")
    
data['ap_2010'].dtypes

## 12. Performing the Left Joins ##

combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], on="DBN", how="left")

combined = combined.merge(data["graduation"], on="DBN", how="left")


combined.shape

## 13. Performing the Inner Joins ##

combined = combined.merge(data["class_size"], on="DBN", how="inner")

combined = combined.merge(data["demographics"], on="DBN", how="inner")

combined = combined.merge(data["survey"], on="DBN", how="inner")

combined = combined.merge(data["hs_directory"], on="DBN", how="inner")

combined.shape

## 15. Filling in Missing Values ##

combined = combined.fillna(combined.mean()) 

combined = combined.fillna(0) 

combined.head(3)

## 16. Adding a School District Column for Mapping ##

def f(s):
    return s[:2]

combined['school_dist'] = combined['DBN'].apply(f)

combined['school_dist'].head(3)