import streamlit as st
import pandas as pd

st.header("NFL Kickers Points Above Average")
data = pd.read_csv("kickerseasons.csv").drop("Unnamed: 0",1)
data = data[["Name","Season","Team","Total","50+","40-49","30-39","20-29","0-19","XP","Age"]]
data = data[abs(data["XP"])+abs(data["0-19"])+abs(data["20-29"])+abs(data["30-39"])+abs(data["40-49"])+abs(data["50+"])!= 0]
seasons = st.slider("Seasons",1961,2020,(1961,2020))
data = data[data["Season"]>= seasons[0]]
data = data[data["Season"]<= seasons[1]]
cumulative = st.checkbox("Career Totals")
st.write("The rating in each column represents the Points Above Average for each kicker, adjusted for the league averages in each season.")
if cumulative:
    x = data.groupby("Name").sum()
    x = x.drop(["Season","Age"],1)
    x["Seasons"] = data.groupby("Name")["Season"].count()
    data = x
data = data.sort_values(by = "Total", ascending = False)
st.dataframe(data.style.format({"0-19": "{:.1f}","20-29": "{:.1f}","30-39": "{:.1f}","40-49": "{:.1f}","50+": "{:.1f}","XP": "{:.1f}","Total": "{:.1f}"}),width = 99999, height = 2000)