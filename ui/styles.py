import streamlit as st

SCORE_CARD_CSS = """
<style>

.score-card{
    background:#1E1E1E;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 0 10px rgba(255,255,255,0.05);
}

.circle{
    width:140px;
    height:140px;
    margin:auto;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:34px;
    font-weight:bold;
    color:white;
}

.score-title{
    font-size:18px;
    font-weight:bold;
    margin-bottom:15px;
}

.score-label{
    margin-top:12px;
    font-size:18px;
    color:#00d084;
}

</style>
"""


def inject_global_styles():
    st.markdown(SCORE_CARD_CSS, unsafe_allow_html=True)