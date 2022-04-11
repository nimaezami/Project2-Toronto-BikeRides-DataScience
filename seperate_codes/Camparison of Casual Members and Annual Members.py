#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data_days = pd.DataFrame()
data_days['rides']=data_merged.groupby('trip_start_time').size().resample('D').sum()
data_days['annual_members']=data_merged[data_merged['user_type']=='Annual Member'].groupby('trip_start_time').size().resample('D').sum()
data_days['casual_members']=data_merged[data_merged['user_type']=='Casual Member'].groupby('trip_start_time').size().resample('D').sum()
data_days['workday']='False'
data_days['day']= data_days.index.dayofweek
for i in range(0,len(data_days['day'])):
    if (data_days['day'][i])<=4:
        data_days['workday'][i]='True'
data_days=data_days.drop(columns=['day'])

#Camparison of Casual Members and Annual Members\n on working and Non-working days
fig, axes = plt.subplots(2,3,figsize=(25, 20))
data_days_2017=data_days.loc['2017']
sns.scatterplot(x=data_days_2017["casual_members"],y=data_days_2017["annual_members"],hue=data_days_2017['workday'],
                ax=axes[0, 0])
axes[0,0].set_title('Daily ride counts 2017')
plt.setp(axes[0,0], xlabel=('Casual Membership'), ylabel=("Annual Membership"))

data_days_2018=data_days.loc['2018']
sns.scatterplot(x=data_days_2018["casual_members"],y=data_days_2018["annual_members"],hue=data_days_2018['workday'],
                ax=axes[0, 1])
axes[0,1].set_title('Daily ride counts 2018')
plt.setp(axes[0,1], xlabel=('Casual Membership'), ylabel=("Annual Membership"))

data_days_2019=data_days.loc['2019']
sns.scatterplot(x=data_days_2019["casual_members"],y=data_days_2019["annual_members"],hue=data_days_2019['workday'],
                ax=axes[0, 2])
axes[0,2].set_title('Daily ride counts 2019')
plt.setp(axes[0,2], xlabel=('Casual Membership'), ylabel=("Annual Membership"))


data_days_2020=data_days.loc['2020']
sns.scatterplot(x=data_days_2020["casual_members"],y=data_days_2020["annual_members"],hue=data_days_2020['workday'],
                ax=axes[1, 0])
axes[1,0].set_title('Daily ride counts 2020')
plt.setp(axes[1,0], xlabel=('Casual Membership'), ylabel=("Annual Membership"))

data_days_2021=data_days.loc['2021']
sns.scatterplot(x=data_days_2021["casual_members"],y=data_days_2021["annual_members"],hue=data_days_2021['workday'],
                ax=axes[1, 1])
axes[1,1].set_title('Daily ride counts 2021')
plt.setp(axes[1,1], xlabel=('Casual Membership'), ylabel=("Annual Membership"))

fig.suptitle('Camparison of Casual Members and Annual Members\n on working and Non-working days')
plt.show()


data_merged_2017=data_merged[data_merged['merge_time']<'2018-1-1']
df_hour_2017 = pd.DataFrame()
df_hour_2017['rides']=data_merged_2017.groupby(data_merged_2017['merge_time']).size()
df_hour_2017['annual_members']=data_merged_2017[data_merged_2017['user_type']=='Annual Member'].groupby(data_merged_2017['merge_time']).size()
df_hour_2017['casual_members']=data_merged_2017[data_merged_2017['user_type']=='Casual Member'].groupby(data_merged_2017['merge_time']).size()
df_hour_2017['hour']=df_hour_2017.index.hour
data_hours_2017=df_hour_2017.groupby(df_hour_2017['hour']).mean()


data_merged_2018=data_merged[(data_merged['merge_time']<'2019-1-1') & (data_merged['merge_time']>='2018-1-1')]
df_hour_2018 = pd.DataFrame()
df_hour_2018['rides']=data_merged_2018.groupby(data_merged_2018['merge_time']).size()
df_hour_2018['annual_members']=data_merged_2018[data_merged_2018['user_type']=='Annual Member'].groupby(data_merged_2018['merge_time']).size()
df_hour_2018['casual_members']=data_merged_2018[data_merged_2018['user_type']=='Casual Member'].groupby(data_merged_2018['merge_time']).size()
df_hour_2018['hour']=df_hour_2018.index.hour
data_hours_2018=df_hour_2018.groupby(df_hour_2018['hour']).mean()

data_merged_2019=data_merged[(data_merged['merge_time']<'2020-1-1') & (data_merged['merge_time']>='2019-1-1')]
df_hour_2019 = pd.DataFrame()
df_hour_2019['rides']=data_merged_2019.groupby(data_merged_2019['merge_time']).size()
df_hour_2019['annual_members']=data_merged_2019[data_merged_2019['user_type']=='Annual Member'].groupby(data_merged_2019['merge_time']).size()
df_hour_2019['casual_members']=data_merged_2019[data_merged_2019['user_type']=='Casual Member'].groupby(data_merged_2019['merge_time']).size()
df_hour_2019['hour']=df_hour_2019.index.hour
data_hours_2019=df_hour_2019.groupby(df_hour_2019['hour']).mean()


data_merged_2020=data_merged[(data_merged['merge_time']<'2021-1-1') & (data_merged['merge_time']>='2020-1-1')]
df_hour_2020 = pd.DataFrame()
df_hour_2020['rides']=data_merged_2020.groupby(data_merged_2020['merge_time']).size()
df_hour_2020['annual_members']=data_merged_2020[data_merged_2020['user_type']=='Annual Member'].groupby(data_merged_2020['merge_time']).size()
df_hour_2020['casual_members']=data_merged_2020[data_merged_2020['user_type']=='Casual Member'].groupby(data_merged_2020['merge_time']).size()
df_hour_2020['hour']=df_hour_2020.index.hour
data_hours_2020=df_hour_2020.groupby(df_hour_2020['hour']).mean()


data_merged_2021=data_merged[(data_merged['merge_time']<'2022-1-1') & (data_merged['merge_time']>='2021-1-1')]
df_hour_2021 = pd.DataFrame()
df_hour_2021['rides']=data_merged_2021.groupby(data_merged_2021['merge_time']).size()
df_hour_2021['annual_members']=data_merged_2021[data_merged_2021['user_type']=='Annual Member'].groupby(data_merged_2021['merge_time']).size()
df_hour_2021['casual_members']=data_merged_2021[data_merged_2021['user_type']=='Casual Member'].groupby(data_merged_2021['merge_time']).size()
df_hour_2021['hour']=df_hour_2021.index.hour
data_hours_2021=df_hour_2021.groupby(df_hour_2021['hour']).mean()


