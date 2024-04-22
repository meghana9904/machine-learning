import streamlit as st
import pandas as pd
import sklearn
import joblib

match = pd.read_csv(r'Data/IPL_Matches_2008_2022.csv')
model = joblib.load('models/log_reg.pkl')
teamnames = sorted(match['Team1'].unique().tolist())
stadiumnames = sorted(match['Venue'].unique().tolist())

col1, col2 = st.columns(2)

with col1:
    batteam = st.selectbox('Batting Team',teamnames)
  

with col2:
    bowteam = st.selectbox('Bowling Team',[i for i in teamnames if i != batteam])
    

stadium = st.selectbox('Stadium',stadiumnames)

col1, col2, col3 = st.columns(3)

target = st.number_input('Target', min_value=1)

with col1:
    over = st.number_input('Number of Overs Completed',min_value=1, max_value=19, step=1)
with col2:
    score = st.number_input('Score',min_value=0, step=1)
with col3:
    wicket = st.number_input('Wickets',min_value=0, max_value=9, step=1)

state = st.button("Predict")
runs_left = target-score
balls_left = 120 - over*6

if state:
    pred = model.predict_proba(pd.DataFrame({
        'BattingTeam':[batteam],
        'BowlingTeam':[bowteam],
        'Venue':[stadium],
        'runs_left':[runs_left],
        'balls_left':[balls_left],	
        'wickets':[10-wicket],
        'CurrentScore':[score],
        'total_run_x':[target],
        'crr':[score/over],
        'rrr':[runs_left*6/balls_left]
    }))
    r_1 = round(pred[0][0]*100)
    r_2 = round(pred[0][1]*100)
    st.header('Wining Probabilty ')
    st.header(f"{batteam}  : {r_2} %")
    st.header(f"{bowteam}  : {r_1} %")