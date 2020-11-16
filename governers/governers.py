# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:28:54 2020

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing
county=pd.read_csv("governors_county.csv")
state=pd.read_csv('governors_state.csv')
candidate=pd.read_csv('governors_county_candidate.csv')

#viewing the data
df=[county,state,candidate]
for i in df:
      print(i.columns)
for i in df:
    print(i.head())      
#votes in candidate and state are diff lets rename
state=state.rename(columns={"votes":"complete_votes"})

for i in df:
    print(i.shape)

#no missing data        
for i in df:
    print(i.isnull().sum())

#exploring & Visualizing COUNTY data
county["actual_percent"]=100*(county.current_votes/county.total_votes)
#11 States
len(county.state.unique())
#864 counties
len(county.county.unique())

#total votes in county and state dataset not equal
for i in range(0,len(state.index)):
    if county.groupby('state')['total_votes'].sum()[i]>state.complete_votes[i]:
        print('Votes more in county')
    elif county.groupby('state')['total_votes'].sum()[i]<state.complete_votes[i]:
        print("Votes more in state")
    else:
        print("Equal")

#average votes per state
total_votes_county={}
for st in county.state.unique():
    total_votes_county[st]=county.loc[county['state']==st,'current_votes'].sum()

#current votes plot
county.groupby('state')['current_votes'].mean().sort_values(ascending=False).plot.bar()
plt.title("Top states according to current votes mean")
plt.show()

county.groupby('state')['current_votes'].sum().sort_values(ascending=False).plot.bar()
plt.title("Top states according to current votes sum")
plt.show()

#more than 100% 
mor_thn_cent=county.loc[county['actual_percent']>100,]
#more than 98%
more_thn_nineight=county.loc[county['percent']>98,]

#attendance by state
#north dakota less than 90%
county.groupby('state')['percent'].mean().sort_values(ascending=True).plot.bar()
plt.ylim(75,100)
plt.title("Attendance")
plt.show()


#best county
#king county
county.groupby('county')['current_votes'].sum().sort_values(ascending=False)[0:5].plot.bar()
plt.title('Top 5 best counties')
plt.show()

print(county.loc[county['county']=="King County",].state.values[0])

#worst county
county.groupby('county')['current_votes'].sum().sort_values()[0:5].plot.bar()
plt.title('Worst 5  counties ')
plt.show()


print(county.loc[county['county']=="Treasure County",].state.values[0])


#box plot
county.actual_percent.plot.box()
plt.title('Outliers in voter percentages')
plt.show()

outliers=county.actual_percent.sort_values(ascending=False)[0:5].index.tolist()
for i in outliers:
    print(county.loc[county.index==i,])

#-------------------------------------------------------------------------------------------------------------------------------
#exploring and visualizing the CANDIDATE data
#members per party
candidate['party'].value_counts().plot.bar()
plt.title('Members per party')
plt.show()
#most members standing for Wayne County
candidate['county'].value_counts()[0:10].plot.bar()
plt.title("Most members per county")
plt.show()
#len(candidate.county)
#multiple candidates of the same party, most for wayne county
candidate.groupby('party')['county'].value_counts().sort_values(ascending=False)[0:10].plot.bar()
plt.title('members per county per party')
plt.show()
#winning governer
candidate.loc[candidate['won']==True,["candidate","state","party"]].value_counts().sort_values(ascending=False)[0:10].plot.bar()
plt.title('winnig governer')
plt.show()

#total votes per state
total_votes_candidate={}
for st in county.state.unique():
    total_votes_candidate[st]=candidate.loc[candidate['state']==st,'votes'].sum()

#votes count is same
print(total_votes_county==total_votes_candidate)

#pie
candidate.loc[candidate['won']==True,["candidate","state","party"]].value_counts()[0:10].plot.pie(label='')