## 1. Geographic Data ##

import pandas as pd
airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')
print(airlines.iloc[1])
print(airports.iloc[1])
print(routes.iloc[1])

## 4. Workflow With Basemap ##

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
m = Basemap(projection = 'merc',llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

## 5. Converting From Spherical to Cartesian Coordinates ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = list(airports['longitude'])
latitudes = list(airports['latitude'])
x, y = m(longitudes, latitudes)

## 6. Generating A Scatter Plot ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
x, y = m(longitudes, latitudes)
m.scatter(x,y,s=1)
plt.show()

## 7. Customizing The Plot Using Basemap ##

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 8. Customizing The Plot Using Matplotlib ##

fig, ax = plt.subplots(figsize=(15, 20))
ax.set_title('Scaled Up Earth With Coastlines')
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

## 9. Introduction to Great Circles ##

geo_routes = pd.read_csv('geo_routes.csv')
geo_routes.head(5)

## 10. Displaying Great Circles ##

fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

def create_great_circles(df):
    for index, row in df.iterrows():
        lon1 =float(row['start_lon'])
        lat1 =float(row['start_lat'])
        lon2 = float(row['end_lon'])
        lat2 = float(row['end_lat'])
        if abs(lat2-lat1) <180 and abs(lon2-lon1) <180:
            m.drawgreatcircle(lon1,lat1,lon2,lat2)
  
dfw = geo_routes[geo_routes['source']=='DFW']

create_great_circles(dfw)
plt.show()


            
            
