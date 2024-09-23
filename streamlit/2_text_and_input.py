import streamlit as st
st.title("Streamlit Text Input Examples")
name = st.text_input("Enter your name")
feedback = st.text_area("Enter your feedback here")
age = st.number_input("Enter your age ")
date = st.date_input("Select a date")
time = st.time_input("Pick a time")
color = st.color_picker("Pick a color")
color_sub = st.color_picker("Pick a color for subheading")
mobile_no = st.number_input
# display inputs 
st.write("Name",name)
st.write("Feedback", feedback)
st.write("Age",age)
st.write("Date",date)
st.write("time",time)
st.write("Color",color)

html_code = """
<h1 style = "color:{};">A Color changing heading</h1>
<p style = "color:{};">A color changing paragraph.</p>
""".format(color,color_sub)
st.markdown(html_code,unsafe_allow_html=True)