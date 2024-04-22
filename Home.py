import streamlit as st

st.header('IPL - Indian Premier League :cricket_bat_and_ball:')

col11,col12,col13 =  st.columns([2,8,2])

with col12:
    st.image('data/IPL_Logo.png')
    


with st.expander("History of IPL"):
    st.write("""**History of the Indian Premier League (IPL)**

**Introduction:**
- The Indian Premier League (IPL) is a professional Twenty20 cricket league in India.
- Launched by the Board of Control for Cricket in India (BCCI) in 2008.

**Key Milestones:**
- **2008:** Inaugural season with eight teams representing various cities.
- **2009:** Relocated to South Africa due to general elections in India.
- **2010:** Chennai Super Kings clinched their first title.
- **2011:** The tournament expanded to 10 teams with the addition of Pune Warriors India and Kochi Tuskers Kerala.
- **2012:** Kolkata Knight Riders won their first IPL title.
- **2013:** Mumbai Indians won their first IPL title.
- **2014:** The tournament returned to India after being held in part in the UAE due to the general elections.
- **2015:** Mumbai Indians won their second IPL title.
- **2016:** Sunrisers Hyderabad clinched their first IPL title.
- **2018:** Chennai Super Kings won their third IPL title.
- **2019:** Mumbai Indians won their fourth IPL title, becoming the most successful team.
- **2020:** Due to the COVID-19 pandemic, the tournament was held in the United Arab Emirates.
- **2021:** Chennai Super Kings won their fourth IPL title.

**Format and Teams:**
- Consists of franchise teams representing different cities and states.
- Each team plays a total of 14 matches in the league stage.
- Top four teams qualify for the playoffs, consisting of Qualifier 1, Eliminator, Qualifier 2, and the Final.
- Players from around the world participate, making it a truly global event.

**Impact and Legacy:**
- Revolutionized cricket with its fast-paced format and entertainment value.
- Provides a platform for young talent to showcase their skills alongside international stars.
- Has contributed significantly to the growth of cricket in India and globally.
- Generates substantial revenue through broadcasting rights, sponsorships, and merchandise.

**Conclusion:**
- The IPL has become one of the most-watched cricket leagues globally, captivating audiences with its thrilling matches and star-studded line-ups. It continues to evolve, leaving an indelible mark on the world of cricket.""")
  
  

    
