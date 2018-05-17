## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for file in data_files:
    data[file.replace('.csv', '')] = pd.read_csv('schools/'+file)

## 5. Exploring the SAT Data ##

data['sat_results'].head(5)

## 6. Exploring the Remaining Data ##

for key in data:
    print(data[key].head(5))

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', delimiter="\t", encoding="windows-1252")

d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter="\t", encoding="windows-1252")

survey = pd.concat([all_survey, d75_survey], axis=0)

survey.head(5)

## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]
lst = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey[lst]
data['survey'] = survey

## 11. Inserting DBN Fields ##

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

def f(n):
   s = str(n)
   if len(s) == 2:
        return s
   else:
        return '0'+s

data['class_size']['padded_csd']=data['class_size']["CSD"].apply(f)

data['class_size']['DBN'] = data['class_size']['padded_csd']+data['class_size']['SCHOOL CODE']

data['class_size'].head(5)

## 12. Combining the SAT Scores ##

cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score']+data['sat_results']['SAT Critical Reading Avg. Score']+data['sat_results']['SAT Writing Avg. Score']

data['sat_results']['sat_score'].head(5)

## 13. Parsing Geographic Coordinates for Schools ##

import re

def f(s):
    location  = re.findall('\(.+\)', s)
    lat = location[0].split()[0].strip('(°,')
    return lat

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(f)

data['hs_directory'].head(3)


## 14. Extracting the Longitude ##

import re

def f(s):
    location  = re.findall('\(.+\)', s)
    longitude = location[0].split()[1].strip(')°,')
    return longitude

data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(f)

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors="coerce")

data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors="coerce")

data['hs_directory'].head(3)