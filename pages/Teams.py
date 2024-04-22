import streamlit as st
import pandas as pd

def check(match, team):
    return len(match[(match['Team1'] == team) | (match['Team2'] == team)])

def count(S, team):
    try:
        return S[S.index == team].values[-1]
    except:
        return 0

match = pd.read_csv(r'data/IPL_Matches_2008_2022.csv')
win = match.groupby(['WinningTeam'])['WinningTeam'].count()
playoff = match[match['MatchNumber'].isin(['Qualifier 1', 'Eliminator', 'Semi Final'])]
final = match[match['MatchNumber'].isin(['Final'])]['WinningTeam'].value_counts()
teamnames = sorted(match['Team1'].unique().tolist())
team = st.selectbox('Select Team', teamnames)

col2 = st.columns(2)

col2[0].write("Total Matches: " + str(check(match, team)))
col2[0].write("Total Won: " + str(win[win.index == team].iloc[-1]))
col2[0].write("Playoff Qualifies: " + str(check(playoff, team)))
col2[0].write("Title Won: " + str(count(final, team)))
col2[0].write("Toss Won: " + str(count(match['TossWinner'].value_counts(), team)))
