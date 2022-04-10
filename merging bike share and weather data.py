#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#weather part1
path='weather'
weather_filenames1 = [file for file in os.listdir(path) if '6158359' in file]
for item in weather_filenames1:
    if ('2019' in item) or ('2021' in item):
        weather_filenames1.remove(item)


for item in weather_filenames1:
    if ('2020' in item):
        weather_filenames1.remove(item)

df_weather=[]
for i in range(len(weather_filenames1)):
    path='weather'
    filename=weather_filenames1[i]
    file_path = os.path.join(path, filename)
    file = pd.read_csv(file_path)
    df_weather.append(file)
weather_data1 = pd.concat(df_weather)
#put datetime as index
weather_data1.index=pd.DatetimeIndex(weather_data1['Date/Time'])
weather_data1=weather_data1.drop(columns=['Date/Time'])
#localize datetime
weather_data1.index=weather_data1.index.tz_localize('EST')
weather_data1.head()

#weather part2
path='weather'
weather_filenames2 = [file for file in os.listdir(path) if '6158359' in file]
for item in weather_filenames1:
    if ('2017' in item) or ('2018' in item):
        weather_filenames2.remove(item)

for item in weather_filenames2:
    if ('2021' in item):
        weather_filenames2.remove(item)
df_weather=[]
for i in range(len(weather_filenames2)):
    path='weather'
    filename=weather_filenames2[i]
    file_path = os.path.join(path, filename)
    file = pd.read_csv(file_path)
    df_weather.append(file)
weather_data2 = pd.concat(df_weather)
#put datetime as index
weather_data2.index=pd.DatetimeIndex(weather_data2['Date/Time'])
weather_data2=weather_data2.drop(columns=['Date/Time'])
#localize datetime
weather_data2.index=weather_data2.index.tz_localize('EST')
weather_data2=weather_data2.drop(columns=['Precip. Amount (mm)','Precip. Amount Flag'])

#weather part3
path='weather'
weather_filenames3 = [file for file in os.listdir(path) if '2021' in file]

df_weather=[]
for i in range(len(weather_filenames3)):
    path='weather'
    filename=weather_filenames3[i]
    file_path = os.path.join(path, filename)
    file = pd.read_csv(file_path)
    df_weather.append(file)
weather_data3 = pd.concat(df_weather)
#rename columns based on part1
weather_data3=weather_data3.rename(columns={'Date/Time (LST)':'Date/Time','Time (LST)':'Time'})
col_weather2=['Longitude (x)', 'Latitude (y)', 'Station Name', 'Climate ID',
       'Date/Time', 'Year', 'Month', 'Day', 'Time', 'Temp (°C)', 'Temp Flag',
       'Dew Point Temp (°C)', 'Dew Point Temp Flag', 'Rel Hum (%)',
       'Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag',
       'Wind Spd (km/h)', 'Wind Spd Flag', 'Visibility (km)',
       'Visibility Flag', 'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx',
       'Hmdx Flag', 'Wind Chill', 'Wind Chill Flag', 'Weather',
       'Precip. Amount (mm)', 'Precip. Amount Flag']
weather_data3=weather_data3[col_weather2]
#put datetime as index
weather_data3.index=pd.DatetimeIndex(weather_data3['Date/Time'])
weather_data3=weather_data3.drop(columns=['Date/Time'])
#localize datetime
weather_data3.index=weather_data3.index.tz_localize('EST')
#drop extra columns
weather_data3=weather_data3.drop(columns=['Precip. Amount (mm)','Precip. Amount Flag'])

#concatinate all part of weather data
frames = [weather_data1,weather_data2,weather_data3]
weather_data=pd.concat(frames)
weather_data.index=pd.to_datetime(weather_data.index)
weather_data.head()

#visualizing temperature data from weather
plt.figure(figsize=(10, 5))
ax = sns.lineplot(x=weather_data.index, y=weather_data['Temp (°C)'])
ax.set_title('Temperature in the city of Toronto between 2017 and 2022')
ax.set_xlabel('Date-Time')
ax.set_ylabel('Temperature °C')
plt.show();
#merge trip data and weather data
data_merged=trips_data.merge(weather_data,how='left', left_on='merge_time', right_on=weather_data.index)

