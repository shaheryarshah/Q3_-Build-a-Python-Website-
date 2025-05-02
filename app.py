# app.py

import streamlit as st

# Title of the website
st.title("🚀 Welcome to My Python Website!")

# Subtitle
st.subheader("A simple Streamlit app built in 5 minutes")

# User input
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}! 👋 Nice to meet you.")
    else:
        st.warning("Please enter your name above!")

# Optional extras
st.markdown("---")
st.info("This site is powered by [Streamlit](https://streamlit.io)")
