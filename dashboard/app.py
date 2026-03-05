import streamlit as st
import json


st.title("YouTube Viral Dashboard")

with open("../data/niche_rank.json") as f:

    data = json.load(f)

for niche in data:

    st.header(niche)

    for v in data[niche]:

        st.write(v["title"])
