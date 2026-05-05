import streamlit as st
from utils import calculate_similarity

st.title("AI Resume Analyzer")

resume = st.text_area("Paste your Resume")
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):
    score = calculate_similarity(resume, jd)
    st.write("Match Score:", round(score * 100, 2), "%")