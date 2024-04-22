import streamlit as st
import numpy as np
import pandas as pd

st.header('Player Performance Overview :cricket_bat_and_ball:')
#------------------------------------------------------------------------------------------------------------------------
merged_ipl = pd.read_csv("data\IPL_Ball_by_Ball_2008_2022.csv")
players = merged_ipl['batter'].unique().tolist()
players.extend(merged_ipl['bowler'].unique().tolist())
players = list(set(players))
players.sort()
player = st.selectbox('Select the Player: ', players)

player_filter_batting = merged_ipl[merged_ipl['batter']==player]
player_filter_bowling = merged_ipl[merged_ipl['bowler']==player]

no_of_matches_played = merged_ipl[(merged_ipl['batter']==player)]["ID"].nunique()

total_runs = merged_ipl[(merged_ipl['batter']==player)]['total_run'].sum()

total_balls = merged_ipl[(merged_ipl['batter']==player)]['ballnumber'].count()

strike_rate = round((total_runs / total_balls) * 100, 2)

st.subheader(f'Summary about {player}')
#-------------------------------------------------------------------------------------------------------------------------
st.divider()
st.subheader('Batting :')

col11,col12,col13,col14 =  st.columns(4)

with col11:
    st.metric('No.of Matches Played: ', value=no_of_matches_played)

with col12:
    st.metric('Total Runs: ', value=total_runs)

with col13:
    st.metric('Total Balls Faced: ', value=total_balls)

with col14:
    st.metric('Strike Rate: ', value=strike_rate)
#---------------------------------------------------------------------------------------------------------------------
highest_runs = player_filter_batting.groupby('ID')['total_run'].sum().max()
_4s = player_filter_batting[player_filter_batting['total_run']==4]['total_run'].count()
_6s = player_filter_batting[player_filter_batting['total_run']==6]['total_run'].count()
_100s = (player_filter_batting.groupby(['ID', 'batter'])['total_run'].sum() >= 100).sum()

col21,col22,col23,col24 =  st.columns(4)

with col21:
    st.metric('Highest Runs: ', value=highest_runs)

with col22:
    st.metric("Total Fours (4's): ", value=_4s)

with col23:
    st.metric("Total Sixes (6's): ", value=_6s)

with col24:
    st.metric("Total 100's : ", value=_100s)
#---------------------------------------------------------------------------------------------------------------------
no_of_matches_played_bowling = merged_ipl[(merged_ipl['bowler']==player)]['ID'].nunique()
total_runs_given = player_filter_bowling['total_run'].sum()
no_of_balls_delivered = player_filter_bowling['ballnumber'].count()
no_of_wickets_taken = player_filter_bowling['isWicketDelivery'].sum()

st.divider()
st.subheader('Bowling :')

col31,col32,col33,col34 =  st.columns(4)

with col31:
    st.metric('No.of Matches Bowling: ', value=no_of_matches_played_bowling)

with col32:
    st.metric('Total Runs Given: ', value=total_runs_given)

with col33:
    st.metric('Total Balls Delivered: ', value=no_of_balls_delivered)

with col34:
    st.metric('Wickets : ', value=no_of_wickets_taken)
