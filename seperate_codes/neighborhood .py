#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import geopandas as gpd
#load neighbourhoods data
neighbourhoods = gpd.read_file('neighborhood/toronto_neighbourhoods.shp')
# View GeoDataFrame
neighbourhoods.head()

neighbourhoods=neighbourhoods.drop(neighbourhoods.columns.difference(['geometry','FIELD_8']), axis=1)
neighbourhoods=neighbourhoods.rename(columns={'FIELD_8':'name'})
neighbourhoods['name']=neighbourhoods['name'].str.split('(').str[0].str.rstrip()
# View GeoDataFrame
neighbourhoods.head()
bikeshare_stations_gdf = gpd.GeoDataFrame(bikeshare_stations,geometry=gpd.points_from_xy(bikeshare_stations['lon'],
                                                                   bikeshare_stations['lat']))

# View DataFrame
bikeshare_stations_gdf.head()
#set same crs
neighbourhoods = neighbourhoods.to_crs(epsg=26917)
bikeshare_stations_gdf = bikeshare_stations_gdf.to_crs(epsg=26917)
#join bikeshare_station with neighbourhood
import geopandas
merge_station_neighbourhood=geopandas.sjoin(bikeshare_stations_gdf,neighbourhoods)
bikeshare_stations_gdf['neighbourhood']=merge_station_neighbourhood['name_right']
# View GeoDataFrame
bikeshare_stations_gdf.head()
#merge data_merged with neighbourhood on departure
data_merged_neighbourhood_departure=data_merged.merge(bikeshare_stations_gdf,how='left',left_on='station_id_from', 
                                                     right_on='station_id')
data_merged_neighbourhood_departure.head()
#merge data_merged with neighbourhood on end
data_merged_neighbourhood_end=data_merged.merge(bikeshare_stations_gdf,how='left',left_on='station_id_to', 
                                                     right_on='station_id')
data_merged_neighbourhood_end.head()

#group by neighbourhood
data_ride_neighbourhood = pd.DataFrame()
data_ride_neighbourhood['departure_rides']=data_merged_neighbourhood_departure.groupby('neighbourhood').from_station_id.count().sort_values(
    ascending=False)
data_ride_neighbourhood['end_rides']=data_merged_neighbourhood_end.groupby('neighbourhood').to_station_id.count().sort_values(
    ascending=False)
data_ride_neighbourhood.head()

