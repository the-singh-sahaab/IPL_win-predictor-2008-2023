import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('drive-download\IPL\pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    ballingteam = st.selectbox('Select the batting team',sorted(teams))
with col2:
    BattingTeam = st.selectbox('Select the bowling team',sorted(teams))

City = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wicket_left = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wicket_left = 10 - wicket_left
    current_run_rate = score/overs
    required_run_rate = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'ballingteam':[ballingteam],'BattingTeam':[BattingTeam],'City':[City],'runs_left':[runs_left],'balls_left':[balls_left],'wicket_left':[wicket_left],'total_run_x':[target],'current_run_rate':[current_run_rate],'required_run_rate':[required_run_rate]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(ballingteam + "- " + str(round(win*100)) + "%")
    st.header(BattingTeam + "- " + str(round(loss*100)) + "%")