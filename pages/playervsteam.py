import streamlit as st
import pandas as pd
import time

df = pd.read_csv('data\merged_data.csv')

players_list = (list(df.batter.unique()))
players_list.insert(0, 'None')
player_name = st.selectbox('Choose Player',players_list)

teams_list = (list(df.Team1.unique()))
teams_list.insert(0, 'None')
team = st.selectbox('Choose Opponent Team',teams_list)

res1 = pd.DataFrame()  # Initialize empty DataFrame
res2 = pd.DataFrame()

if st.button('Submit'):

    if (player_name == 'None') & (team == 'None'):
        st.write("##### Select your Player and Team")
    elif (player_name != 'None') & (team == 'None'):
        st.write('##### Select Opponent Team')
    elif (player_name == 'None') & (team != 'None'):
        st.write('##### Select your Player Team')
    elif (player_name != 'None') & (team != 'None'):
        st.header(player_name + "'"+'s Statistics Against '+team)

        def player_vs_team(df,player_name,team):
                titles = ['Number of Innings Played','Total Number of Runs','Highest Score','Number of Balls faced', 'Strike Rate',
                        'Batting Average','Number of Outs','Total Number of Fours','Total Number of Sixes','Total Number of DuckOuts',
                        "Number of 50"+"'s","Number of 100"+"'s"]
                
                values = []
                
                play_vs_team = df[(df.batter == player_name) & (df.Team2 == team) | (df.batter == player_name) & (df.Team1 == team)]
                
                if len(play_vs_team) > 0:
                    values.append(play_vs_team['ID'].nunique()) # number of innings against
                    
                    runs = play_vs_team.groupby(['ID'])[['batsman_run']].sum().reset_index()['batsman_run'].sum() # total runs
                    values.append(runs)
                    
                    highest_score = play_vs_team.groupby(['ID'])[['batsman_run']].sum().reset_index().sort_values(by='batsman_run',ascending=False)
                    highest_score = highest_score[['batsman_run']].head(1).iloc[0,0]
                    values.append(highest_score)  # highest Score
                    
                    balls_faced = len(play_vs_team[play_vs_team['extra_type'] != 'wides'])
                    values.append(balls_faced)  # Balls faced
                    
                    if balls_faced >0:                               # Strike Rate
                        values.append(round(runs/balls_faced*100,2))
                    else:
                        values.append('--')
                        
                    no_of_outs = len(play_vs_team[play_vs_team['player_out'] == player_name])
                    batting_avg = round(runs / no_of_outs, 2)
        
                    values.append(batting_avg)  # batting Average
                    values.append(no_of_outs)   # number of outs

                    values.append(len(play_vs_team[play_vs_team.batsman_run == 4]))   # number of 4's
                    values.append(len(play_vs_team[play_vs_team.batsman_run == 6]))   # number of 6's
                    
                    duck_ = play_vs_team.groupby(['ID'])[['batsman_run']].sum().reset_index()
                    
                    values.append(len(duck_[duck_.batsman_run == 0]))    # no.of Duckouts
                    values.append(len(duck_[duck_.batsman_run >=50]))    # no.of 50's
                    values.append(len(duck_[duck_.batsman_run >=100]))   # no.of 100's
                    
                    #res_df = pd.DataFrame(columns = ['Batter_Attributes','value'])
                else:
                    for i in range(len(titles)):
                        values.append('--')
                        
                res_df = []
                for i,j in zip(titles,values):
                    new_row = {'Batter_Attributes' : i,'value': str(j)}
                    res_df.append(new_row)
                res_df = pd.DataFrame(res_df)
                    
                return res_df


        def Bowler_vs_team(df,player_name,team):
                titles = ['Total Number of Innings','Total Number of Deliveries','Given Total Number of Runs','Total Number of Wicken taken'
                        ,'Given Total Number of Madiens','Total Number of Dot Balls','Total Economy','Average',
                        'Total Strike Rate','BBM','How many times Taken 4 wickets','How many times Taken more than 5 wickets']
                
                values = []
                
                play_vs_team = df[(df.bowler == player_name) & (df.Team2 == team) | (df.bowler == player_name) & (df.Team1 == team)]

                
                if len(play_vs_team) > 0:
                    
                    num_innings = play_vs_team['ID'].nunique()
                    values.append(num_innings) # number of innings against
                    
                    number_of_delivery = len(play_vs_team[(play_vs_team['extra_type'] == 'legal_delivery')])
                    values.append(number_of_delivery)  # NUmber of deliveries
                    
                    total_runs = play_vs_team['total_run'].sum()
                    values.append(total_runs)  # total runs considered
                    
                    
                    
                    madiens_data = play_vs_team.groupby(['ID','overs'])[['total_run']].sum().reset_index()
                    no_of_madiens = len(madiens_data[madiens_data['total_run'] == 0])
                    values.append(no_of_madiens)    # number of madiens
                    
                    no_of_dot_balls = len(play_vs_team[((play_vs_team['extra_type'] == 'legal_delivery') | (play_vs_team['extra_type'] == 'legbyes') |\
                                        (play_vs_team['extra_type'] == 'byes')) & (play_vs_team['batsman_run'] == 0)])
                    values.append(no_of_dot_balls)  # dot balls
                    
                    # Economy
                    if number_of_delivery > 0:
                        values.append(round(total_runs/number_of_delivery*6,2))
                    else:
                        values.append('--')
        
                   
                    
                   
                    
                    
 


        st.write('#### Batting & Bowling Info')   
        res1 = player_vs_team(df, player_name,team)
        res2 = Bowler_vs_team(df,player_name,team)
        st.table(pd.concat([res1,res2],axis=1))

        
            
    




            