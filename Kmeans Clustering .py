#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#create dataframe per hour group by merge time
data_days1 = pd.DataFrame()
data_days1['rides']=data_trip_weather_merged.groupby('merge_time').size().resample('H').sum()
data_days1['annual_members']=data_trip_weather_merged[data_trip_weather_merged['user_type']=='Annual Member'].groupby('merge_time').size().resample('H').sum()
data_days1['casual_members']=data_trip_weather_merged[data_trip_weather_merged['user_type']=='Casual Member'].groupby('merge_time').size().resample('H').sum()

data_days1_features = pd.pivot_table(data_days1, index=data_days1.index.date, columns=data_days1.index.hour, 
                                     values=['annual_members','casual_members'])

data_days1_features = data_days1_features.fillna(0)
data_days1_features.head()
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
pca = PCA(n_components=48)
principalComponents_surfboard = pca.fit_transform(data_days1_features)

column_name=[]
for i in range(1,49):
    column_name.append('pc'+str(i))
data_days1_features_pcs = pd.DataFrame(data = principalComponents_surfboard,index=data_days1_features.index, columns = column_name)
# View DataFrame
data_days1_features_pcs.head()

lst_var=[data_days1_features_pcs[item].var() for item in data_days1_features_pcs.columns]
variance=pd.Series(lst_var)
Proportion_of_Variance=pd.Series([item/sum(lst_var) for item in lst_var])
Cumulative_Proportion=Proportion_of_Variance.cumsum()/Proportion_of_Variance.sum()
pca_summary = pd.DataFrame([variance, Proportion_of_Variance, Cumulative_Proportion],
                           index=['Variance','Proportion of Variance','Cumulative Proportion'])

pca_summary.columns=column_name
# View DataFrame
pca_summary.head()

plt.figure(figsize=(10, 5))
plt.plot(column_name[:10], Proportion_of_Variance[:10], marker= 'o' ,linestyle= '-')
plt.plot(column_name[:10],Cumulative_Proportion[:10], marker = 'o', linestyle= '-')
plt.legend(['Variance','Cumulative variance'])
plt.xlabel('Principal Components')
plt.ylabel('Proportion of Explained Variance %');


plt.figure(figsize=(10, 5))
plt.scatter(data_days1_features_pcs['pc1'],data_days1_features_pcs['pc2'],c=data_days1_features_pcs.sum(axis=1))
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.colorbar(label='Total Trips')
plt.show()

X=data_days1_features_pcs
inertia = []
for i in range(1, 11):
    kmeans=KMeans(n_clusters=i, init='k-means++', max_iter=300, random_state=0)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(10, 5))
plt.plot(range(1,11),inertia, marker= 'o' ,linestyle= '-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(data_days1_features_pcs)


total_trips = data_days1_features_pcs.sum(axis=1)
sns.scatterplot(x=data_days1_features_pcs['pc1'], 
                y=data_days1_features_pcs['pc2'], 
                hue=kmeans.labels_.astype(str), alpha=0.5)
plt.xlabel('PC1', fontsize=14)
plt.ylabel('PC2', fontsize=14);

from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=4, covariance_type='tied', random_state=0)
gmm.fit(data_days1_features_pcs)

total_trips = data_days1_features_pcs.sum(axis=1)
sns.scatterplot(x=data_days1_features_pcs['pc1'], 
                y=data_days1_features_pcs['pc2'], 
                hue=gmm.predict(data_days1_features_pcs).astype(str), alpha=0.5);

data_days1_features['cluster'] = gmm.predict(data_days1_features_pcs)
data_days1_new = data_days1.join(data_days1_features['cluster'], on=data_days1.index.date)
data_days1_new.head()

by_hour = data_days1_new.groupby(['cluster', data_days1_new.index.time]).mean()
by_hour.head()
import numpy as np
fig, ax = plt.subplots(1, 4, figsize=(20, 5))
hourly_ticks = 4 * 60 * 60 * np.arange(6)

for i in range(4):
    by_hour.loc[i].plot(ax=ax[i], xticks=hourly_ticks)
    ax[i].set_title('Cluster {0}'.format(i), fontsize=16)
    ax[i].set_xlabel('Time', fontsize=14)
    ax[i].set_ylabel('Average Hourly Trips', fontsize=14)
    ax[i].tick_params(axis='x', labelrotation=45)
    
data_days1_new.loc[data_days1_new['cluster'] == 2,'cluster'] = 1
data_days1_new.loc[data_days1_new['cluster'] == 3,'cluster'] = 2
data_days1_new.head()

by_hour = data_days1_new.groupby(['cluster', data_days1_new.index.time]).mean()
by_hour.head()

fig, ax = plt.subplots(1, 3, figsize=(20, 5))
hourly_ticks = 4 * 60 * 60 * np.arange(6)

for i in range(3):
    by_hour.loc[i].plot(ax=ax[i], xticks=hourly_ticks)
    ax[i].set_title('Cluster {0}'.format(i), fontsize=16)
    ax[i].set_xlabel('Time', fontsize=14)
    ax[i].set_ylabel('Average Hourly Trips', fontsize=14)
    ax[i].tick_params(axis='x', labelrotation=45)

