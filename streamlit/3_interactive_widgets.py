import streamlit as st

# title
st.title("Streamlit Interactive widget examples")

button = st.button("Click me")
if button:
    st.write("You clicked me")

check_box = st.checkbox("Check me to enable something!")
if check_box:
    st.write("Checkbox is clicked. Something has happened!!")

radio = st.radio("Choose an Option:",["NLP","DL","CV","ML"])
st.write("You have selected:",radio)

select_box = st.selectbox("Choose an Option:",["NLP","DL","CV","ML"]*10)
st.write("You have selected :",select_box)
multi_option = st.multiselect("Choose an Option:",["NLP","DL","CV","ML"]*10)
st.write(f"Your selection is:{multi_option}")
st.write("Your selection is ",multi_option)
rating = st.slider("Select your rating",min_value=1.0,max_value=5.0,step=0.5)
st.write("Your ratinging is:",rating)
item_slider = st.select_slider("Select a value",['NLP','DL','CV','ML'])
st.write("Your item is:",item_slider)