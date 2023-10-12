#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.base import BaseEstimator
from sklearn.utils.estimator_checks import check_estimator
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from typing import Optional, Union

data = pd.read_csv('Desktop/data.csv', index_col='entry_id')
element_types = pd.read_csv('Desktop/element_types.csv', index_col='id')
players = pd.read_csv('Desktop/players.csv', index_col='id')
teams = pd.read_csv('Desktop/teams.csv', index_col='id')


# In[64]:


print(data.info())

data.head()


# In[5]:


print(element_types.info())

element_types.head()


# In[6]:


print(players.info())

players.head()


# In[7]:


print(teams.info())

teams.head()


# In[8]:


train_data = data[data.event_id < 38]
test_data = data[data.event_id == 38]

print("Training data entries:", train_data.shape[0])
print("Test data entries:", test_data.shape[0])


# In[9]:


removed_cols = ['timestamp', 'fixture_code', 'kickoff_time', 'opposition', 'event_id']

for col in removed_cols:
    del train_data[col]
    del test_data[col]


# In[10]:




plt.figure(figsize=(10, 10))
sns.histplot(x=train_data.response, hue=train_data.status, binwidth=1)


# In[11]:


played_match_1 = train_data[train_data.status == 'a']["minutes_1"] > 0
played_match_2 = train_data[train_data.status == 'a']["minutes_2"] > 0
played_match_3 = train_data[train_data.status == 'a']["minutes_3"] > 0

fig, ax = plt.subplots(1, 3, figsize=(20, 5), sharey=True)
sns.kdeplot(x=train_data[train_data.status == 'a'].response, hue=played_match_1, shade=True, ax=ax[0])
sns.kdeplot(x=train_data[train_data.status == 'a'].response, hue=played_match_2, shade=True, ax=ax[1])
sns.kdeplot(x=train_data[train_data.status == 'a'].response, hue=played_match_3, shade=True, ax=ax[2])


# In[14]:


available_players = train_data[train_data.status == 'a'].copy()

sns.jointplot(x=available_players.form, y=available_players.response, kind='kde', fill=True)
sns.jointplot(x=available_players.points_1, y=available_players.response, kind='kde', fill=True)
sns.jointplot(x=available_players.points_2, y=available_players.response, kind='kde', fill=True)
sns.jointplot(x=available_players.points_3, y=available_players.response, kind='kde', fill=True)


# In[15]:


sns.histplot(x=available_players.response, hue=available_players.is_home, binwidth=1)


# In[16]:


train_data.info()


# In[17]:


train_data = pd.get_dummies(train_data)
test_data  = pd.get_dummies(test_data)

train_data.info()
test_data.info()


# In[18]:


def fill_values(df):
    df['chance_of_playing_this_round'] = df['chance_of_playing_this_round'].fillna(100)
    df.fillna(0, inplace=True)
    
fill_values(train_data)
fill_values(test_data)

train_data.head()


# In[19]:


train_data.info()


# In[20]:




del train_data['player_id']


# In[21]:




features = list(train_data.columns)
features.remove('response')
X_train, y_train = train_data[features].values, train_data['response'].values
print(X_train.shape)
print(y_train.shape)


# In[22]:


scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
print(X_train)


# In[23]:


model1 = LinearRegression()
model1.fit(X_train, y_train)


# In[24]:


player_ids = test_data['player_id'].values 
del test_data['player_id']
X_test, y_test = test_data[features].values, test_data['response'].values
X_test = scaler.transform(X_test)


# In[62]:


def model_to_predictions(model):
    predictions = model.predict(X_test)
    predictions = [[player_ids[i], predictions[i], y_test[i]] for i in range(len(player_ids))]
    predictions = pd.DataFrame(predictions, columns=['id', 'prediction', 'actual']).set_index('id')
    predictions = predictions.join(players, on='id')
    return predictions

model_to_predictions(model1).sort_values('prediction', ascending=False).head(40)


# In[26]:


model1.score(X_test, y_test)


# In[27]:


def plot_predictions(model):
    sns.regplot(x=model.predict(X_test), y=y_test)
    plt.xlabel('Prediction')
    plt.ylabel('Response')
    
plot_predictions(model1)


# In[28]:




model2 = RandomForestRegressor(n_estimators=500, max_depth=10, min_samples_split=2, min_samples_leaf=5)
model2.fit(X_train, y_train)


# In[61]:



model_to_predictions(model2).sort_values('prediction', ascending=False).head(40)


# In[30]:


model2.score(X_test, y_test)


# In[31]:




plot_predictions(model2)


# In[ ]:




