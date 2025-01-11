
import streamlit as st

st.set_page_config (page_title="Site Simplify",page_icon="")

st.title("Site Simplify")


with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")
