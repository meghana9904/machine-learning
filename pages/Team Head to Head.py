import streamlit as st
import pandas as pd

def check(match,team1,team2):
    return len(match[((match['Team1'] == team1) | (match['Team2'] == team1)) &
                     ((match['Team1'] == team2) | (match['Team2'] == team2))])

def filter(match,team1,team2):
    return match[((match['Team1'] == team1) | (match['Team2'] == team1)) &
                     ((match['Team1'] == team2) | (match['Team2'] == team2))]

match = pd.read_csv(r'data/IPL_Matches_2008_2022.csv')
teamnames = sorted(match['Team1'].unique().tolist())

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox('Team 1',teamnames)
    

with col2:
    team2 = st.selectbox('Team 2',[i for i in teamnames if i != team1])
    

st.write('Total Matches Played',check(match,team1,team2))