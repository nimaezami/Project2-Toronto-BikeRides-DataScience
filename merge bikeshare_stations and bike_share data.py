#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#loading bikeshare_stations
bikeshare_stations = pd.read_csv('stations/bikeshare_stations.csv')

stations_start = trips_data[['from_station_id', 'from_station_name']]
stations_end = trips_data[['to_station_id', 'to_station_name']]
stations_start.columns = stations_end.columns = ['station_id', 'name']

# Extracts the unique station ID and name combination from the from_station and to_station columns
stations = pd.concat([stations_start, stations_end]).dropna(how='all').drop_duplicates().reset_index(drop=True)

from fuzzywuzzy import fuzz
# Separate the stations without station IDs
no_ids = stations[stations['station_id'].isnull()]
for idx, miss in no_ids.iterrows():
    max_score = 0
    
    # Compare the similarity of the station without ID to each station in the API data
    for i, exist in bikeshare_stations[['station_id', 'name']].iterrows():
        score = fuzz.ratio(miss['name'], exist['name'])
        
        if score > 80 and score > max_score:
            max_score = score
            no_ids.at[idx, 'station_id'] = exist['station_id']
    
    # Warn if the station was not able to be matched
    if max_score <= 80:
        print('WARN: {0} station could not be matched to an existing station'.format(miss['name']))
        
# Remove all stations that were not matched
no_ids = no_ids.dropna()

#concatinate trip_data and stations
stations = pd.concat([stations[~stations['station_id'].isnull()], no_ids])             .merge(bikeshare_stations[['station_id', 'lat', 'lon']], how='inner', on='station_id')             .drop_duplicates()
             
trips_data = trips_data.merge(stations, how='inner', left_on='from_station_name', right_on='name')        .merge(stations, how='inner', left_on='to_station_name', right_on='name', suffixes=['_from', '_to'])        .drop_duplicates()

trips_data = trips_data[[x for x in trips_data.columns if not x.endswith('_station_id') and not x.endswith('_station_name') and x != 'trip_stop_time']]

