import streamlit as st
from sentence_transformers import SentenceTransformer


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# Shared model instance used across the app
model = load_model()