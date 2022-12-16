from library import *
import streamlit as st
import pandas as pd

countries = ['Sri Lanka','United States','India','Japan','China']
statistics = ['cases','deaths','recovered']
country = st.selectbox('Select Your Country',countries)

st.write('Your Selected Country Is',countries)
days = st.sidebar.slider('The Number Of Days You Want',min_value=1,max_value=200)
s_stats = st.sidebar.multiselect('Select Statistics',statistics)

hist_cases = get_historic_cases(country,days)
hist_deaths = get_historic_deaths(country,days)
hist_recovers = get_historic_recoveries(country,days)

cases_df = pd.concat([hist_cases,hist_deaths,hist_recovers],axis=1).astype(int)

daily_cases = get_daily_cases(country,days)
daily_deaths = get_daily_deaths(country,days)
daily_recovers = get_daily_recoveries(country,days)

daily_df = pd.concat([daily_cases,daily_deaths,daily_recovers],axis=1).astype(int)

yest_cases = get_yesterday_cases(country)
yest_deaths = get_yesterday_deaths(country)
yest_recovers = get_yesterday_recoveries(country)

st.metric('Country',country)
st.metric('Yesterday Cases',yest_cases)
st.metric('Yesterday Deaths',yest_deaths)
st.metric('Yesterday Recoveries',yest_recovers)

st.line_chart(daily_df)
st.line_chart(daily_df[s_stats])


