import streamlit as st
import numpy as np
import pandas as pd

auction = pd.read_csv('data/auction.csv')
auction['Winning bid'] = auction['Winning bid'].str.replace(',', '')
auction['Winning bid'] = auction['Winning bid'].astype(float)
st.header('Auction')
years_list = auction['Year'].unique()
year = st.selectbox('Select Year: ', (years_list))
teams = auction[auction['Year'] == year]['Team'].unique()
team = st.selectbox('Select Team: ', (teams))
auc_df = auction[(auction['Year'] == year) & (auction['Team'] == team)]
sorted = auc_df.sort_values(by='Winning bid', ascending=False)
st.divider()
st.markdown(f'{team} Players Winning Bid in the Year {year}')
st.dataframe(data=sorted.iloc[:, 1:])

