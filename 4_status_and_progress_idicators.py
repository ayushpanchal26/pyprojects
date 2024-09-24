import streamlit as st
import time

# Title 
st.title("Streamlit Status and Progress Indicator Examples")
st.markdown("## Empty Element")

empty = st.empty()
empty.text("This text will be replaced after 5 seconds")
time.sleep(5)

empty.text("This is new text data")

# Progress bar
progress = st.progress(0)
status_text = st.empty()
for i in range(101):
    time.sleep(0.1)
    progress.progress(i)
    status_text.text(f"Progress: {i}")

status_text.text(f"Progress:Done ")

with st.spinner("Waiting..."):
    time.sleep(5)
    # load large files here


st.success("Process is Done!!")
st.warning("This is error")
st.info("This is information")
st.error("This is error")

st.snow()