import streamlit as st

st.title("My First Python Website")
st.write("Welcome to this basic Streamlit app!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name} 👋")
