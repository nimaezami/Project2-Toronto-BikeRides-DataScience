#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing libraries
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Bike_share part1
path='bike'
trips_filenames1 = [filename for filename in os.listdir(path) if ('bike_share_2017' in filename) or ('bike_share_2018' in filename)]
#reading and concatinating files in part1
df_bike=[]
for i in range(len(trips_filenames1)):
    filename1=trips_filenames1[i]
    file_path1 = os.path.join(path, filename1)
    file_bike = pd.read_csv(file_path1)
    df_bike.append(file_bike)
trips_data1 = pd.concat(df_bike)

# Let's remove double spaces from the column names
trips_data1.columns = [' '.join(col.split()) for col in trips_data1.columns]  
#standardization of timezone
trips_data1["trip_start_time"]=pd.to_datetime(trips_data1["trip_start_time"], format='%Y-%m-%d %H:%M (%Z)')
trips_data1["trip_stop_time"]=pd.to_datetime(trips_data1["trip_stop_time"], format='%Y-%m-%d %H:%M (%Z)')
#trips_data['trip_start_time'] rounded to the nearest hour
trips_data1['merge_time']=trips_data1['trip_start_time'].dt.floor('H')

# Bike_share part2
path='bike'
trips_filenames2 = [filename for filename in os.listdir(path) if ('bike_share_2019' in filename) or ('bike_share_2020' in filename)]
trips_filenames2.remove('bike_share_2020-11.csv')
trips_filenames2.remove('bike_share_2020-12.csv')

#reading and concatinating files in part2
df_bike=[]
for i in range(len(trips_filenames2)):
    filename1=trips_filenames2[i]
    file_path1 = os.path.join(path, filename1)
    file_bike = pd.read_csv(file_path1)
    df_bike.append(file_bike)
trips_data2 = pd.concat(df_bike)

# Let's remove double spaces from the column names
trips_data2.columns = [' '.join(col.split()) for col in trips_data2.columns]     
#renaming columns based on part1
trips_data2=trips_data2.rename(columns={'Trip Id':'trip_id','Trip Duration':'trip_duration_seconds',
                                        'Start Station Id':'from_station_id','Start Time':'trip_start_time',
                                        'Start Station Name':'from_station_name','End Station Id':'to_station_id',
                                        'End Time':'trip_stop_time','End Station Name':'to_station_name',
                                        'User Type':'user_type'})
#dropping extra unwanted columns
trips_data2=trips_data2.drop(columns=['Subscription Id','Bike Id'])
#changing sequence of columns based on part1
col2=['trip_id','trip_start_time','trip_stop_time','trip_duration_seconds','from_station_id','from_station_name','to_station_id','to_station_name','user_type']
trips_data2=trips_data2[col2]
#standardization of timezone
trips_data2["trip_start_time"]=pd.to_datetime(trips_data2["trip_start_time"], format='%d/%m/%Y %H:%M:%S (%Z)')
trips_data2["trip_stop_time"]=pd.to_datetime(trips_data2["trip_stop_time"], format='%d/%m/%Y %H:%M:%S (%Z)')
#trips_data['trip_start_time'] rounded to the nearest hour
trips_data2['merge_time']=trips_data2['trip_start_time'].dt.floor('H')

# Bike_share part3
path='bike'
trips_filenames3 = [filename for filename in os.listdir(path) if ('bike_share_2021-1.csv' in filename) or 
                    ('bike_share_2020-11.csv' in filename) or ('bike_share_2020-12.csv' in filename) or 
                    ('bike_share_2021-5.csv' in filename)]
#reading and concatinating files in part3
df_bike=[]
for i in range(len(trips_filenames3)):
    filename1=trips_filenames3[i]
    file_path1 = os.path.join(path, filename1)
    file_bike = pd.read_csv(file_path1)
    df_bike.append(file_bike)
trips_data3 = pd.concat(df_bike)

# Let's remove double spaces from the column names
trips_data3.columns = [' '.join(col.split()) for col in trips_data3.columns]
#renaming columns based on part1
trips_data3=trips_data3.rename(columns={'Trip Id':'trip_id','Trip Duration':'trip_duration_seconds',
                                        'Start Station Id':'from_station_id','Start Time':'trip_start_time',
                                        'Start Station Name':'from_station_name','End Station Id':'to_station_id',
                                        'End Time':'trip_stop_time','End Station Name':'to_station_name',
                                        'User Type':'user_type'})
#changing sequence of columns based on part1
col3=['trip_id','trip_start_time','trip_stop_time','trip_duration_seconds','from_station_id','from_station_name','to_station_id','to_station_name','user_type']
trips_data3=trips_data3[col3]

#standardization of timezone
trips_data3["trip_start_time"]=pd.to_datetime(trips_data3["trip_start_time"], format='%d/%m/%Y %H:%M:%S (%Z)')
trips_data3["trip_stop_time"]=pd.to_datetime(trips_data3["trip_stop_time"], format='%d/%m/%Y %H:%M:%S (%Z)')

#trips_data['trip_start_time'] rounded to the nearest hour
trips_data3['merge_time']=trips_data3['trip_start_time'].dt.floor('H')

# Bike_share part4
path='bike'
trips_filenames4 = [filename for filename in os.listdir(path) if ('bike_share_2021' in filename)]
trips_filenames4.remove('bike_share_2021-1.csv')
trips_filenames4.remove('bike_share_2021-5.csv')
#reading and concatinating files in part4
df_bike=[]
for i in range(len(trips_filenames4)):
    filename1=trips_filenames4[i]
    file_path1 = os.path.join(path, filename1)
    file_bike = pd.read_csv(file_path1)
    df_bike.append(file_bike)
trips_data4 = pd.concat(df_bike)

# Let's remove double spaces from the column names
trips_data4.columns = [' '.join(col.split()) for col in trips_data4.columns] 
#renaming columns based on part1
trips_data4=trips_data4.rename(columns={'ï»¿Trip Id':'trip_id','Trip Duration':'trip_duration_seconds',
                                        'Start Station Id':'from_station_id','Start Time':'trip_start_time',
                                        'Start Station Name':'from_station_name','End Station Id':'to_station_id',
                                        'End Time':'trip_stop_time','End Station Name':'to_station_name',
                                        'User Type':'user_type'})
#changing sequence of columns based on part1
col4=['trip_id','trip_start_time','trip_stop_time','trip_duration_seconds','from_station_id','from_station_name','to_station_id','to_station_name','user_type']
trips_data4=trips_data4[col4]
#standardization of timezone
trips_data4["trip_start_time"]=pd.to_datetime(trips_data4["trip_start_time"], format='%d/%m/%Y %H:%M:%S (%Z)')
trips_data4["trip_stop_time"]=pd.to_datetime(trips_data4["trip_stop_time"], format='%d/%m/%Y %H:%M:%S (%Z)')
#trips_data['trip_start_time'] rounded to the nearest hour
trips_data4['merge_time']=trips_data4['trip_start_time'].dt.floor('H')

frames = [trips_data1,trips_data2,trips_data3,trips_data4]
trips_data=pd.concat(frames)

#changing dates to datetime format
trips_data.trip_start_time=pd.to_datetime(trips_data.trip_start_time,utc=True).dt.tz_convert('EST')
trips_data.merge_time=pd.to_datetime(trips_data.merge_time,utc=True).dt.tz_convert('EST')

#standardization user_type values
trips_data.loc[trips_data['user_type']=='Member','user_type']='Annual Member'
trips_data.loc[trips_data['user_type']=='Casual','user_type']='Casual Member'

