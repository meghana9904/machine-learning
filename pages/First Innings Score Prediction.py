import streamlit as st
import pandas as pd
import sklearn
import joblib

match = pd.read_csv(r'data/IPL_Matches_2008_2022.csv')
model = joblib.load('models\Lnr_Reg.pkl')
teamnames = sorted(match['Team1'].unique().tolist())
stadiumnames = sorted(match['Venue'].unique().tolist())

col1, col2 = st.columns(2)

with col1:
    batteam = st.selectbox('Batting Team',teamnames)
    

with col2:
    bowteam = st.selectbox('Bowling Team',[i for i in teamnames if i != batteam])
    

stadium = st.selectbox('Stadium',stadiumnames)

col1, col2, col3 = st.columns(3)

with col1:
    over = st.number_input('Number of Overs Completed',min_value=1, max_value=19, step=1)
with col2:
    score = st.number_input('Score',min_value=0, step=1)
with col3:
    wicket = st.number_input('Wickets',min_value=0, max_value=9, step=1)

state = st.button("Predict")

if state:
    pred = model.predict(pd.DataFrame({
        'BattingTeam':[batteam],
        'BowlingTeam':[bowteam],
        'Venue':[stadium],
        'Overs':[over],
        'CurrentScore':[score],	
        'Wicket':[wicket]
    }))
    st.metric('Projected Score',str(int(pred[-1])))
