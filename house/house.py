# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:20:51 2020

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

state=pd.read_csv('house_state.csv')
candidate=pd.read_csv('house_candidate.csv')

df=[state,candidate]
for i in df:
    print(i.head())
for i in df:
    print(i.info())
for i in df:
    print(i.columns)
    
#EDA STATE
state['district_1']=state.district.apply(lambda x: x.split(" ")[0])
state['district_1']=state.district_1.apply(lambda x: x.replace("'s",''))
state['district_2']=state.district.apply(lambda x:x.split(" ")[1:3])
state['district_2']=state.district_2.apply(lambda x:" ".join(x))   #didnt have to do this redundant
state['actual_percent']=100*(state.current_votes/state.total_votes)
state['actual_percent'].fillna(0,inplace=True)
#united comes first
state.groupby('district_1')['current_votes'].sum().sort_values(ascending=False)[1:11].plot.bar(color=['r','g','b'])
plt.xlabel('state')
plt.title('total current votes')
plt.ylabel('No of votes x 1000000')
plt.show()

#statewise attendance
for i in state.district_1.unique():
    state.loc[state['district_1']==i,['district','actual_percent']].plot.bar()
    plt.title(i)
    plt.xlabel("Districts")
    plt.ylabel("Percentage of attendance")
    plt.show()

#best state
state.groupby('district_1')['actual_percent'].mean().sort_values(ascending=False)[0:10].plot.bar()
plt.title("Best states")
plt.xlabel("State")
plt.ylabel('Attendance')
plt.show()

#worst state
state.groupby('district_1')['actual_percent'].mean().sort_values()[0:10].plot.bar()
plt.title("Worst states")
plt.xlabel("State")
plt.ylabel('Attendance')
plt.show()

#best district
state.groupby('district')['actual_percent'].mean().sort_values()[0:10].plot.bar()
plt.title("Worst attendance")
plt.xlabel('Districts')
plt.ylabel('Attendance percentage')
plt.show()

#best district
state.groupby('district')['actual_percent'].mean().sort_values(ascending=False)[0:10].plot.bar()
plt.title("Best attendance")
plt.xlabel('Districts')
plt.ylabel('Attendance percentage')
plt.show()


#-----------------------------------------------------------------------------------------------------------------------------------------------
#EDA CANDIDATE
candidate['state']=candidate.district.apply(lambda x:x.split(' ')[0])
#percent per state
df=candidate.groupby('state')['total_votes'].sum()
df=df.to_frame()
df=df.to_dict()
candidate['complete_votes']=candidate.state.map(df['total_votes'])
candidate['percent_per_state']=100*(candidate.total_votes/candidate.complete_votes)
#percent per district
df=candidate.groupby('district')['total_votes'].sum()
df=df.to_frame()
df=df.to_dict()
candidate['complete_votes_2']=candidate.district.map(df['total_votes'])
candidate['percent']=100*(candidate.total_votes/candidate.complete_votes_2)
candidate.fillna(0,inplace=True)
candidate=candidate.rename(columns={'percent':'percent_per_district','complete_votes':'comp_votes_per_state','complte_votes_2':'comp_votes_per_district'})



