import streamlit as st

#title - provide main title of the web page
st.title("BMI CALCULATOR")

#subheader - used to create the subheader on the given web page
st.sidebar.header("Enter your personal details")

#text_input - used to collect text input
st.sidebar.text_input("Enter your Name")

#radio button - used to select one option
st.sidebar.radio("Select your Gender: ",["Male","Female","Others"])

#number input - used to take anumber as input
st.sidebar.number_input("Enter your age",0,130)

#text area - used to take multiple lines as input
st.sidebar.text_area("Enter your Address:")

#checkbox - input type of selecting input as checkboxes
st.sidebar.write("Select your hobbies:")
st.sidebar.checkbox("Reading")
st.sidebar.checkbox("Playing")
st.sidebar.checkbox("Dancing")
st.sidebar.checkbox("Singing")
st.sidebar.checkbox("Browsing the internet")

#taking weight as input
weight= st.number_input("Enter your weight in KGS",step=0.1)
#taking height as input
height= st.number_input("Enter your height in Cms",0.1)

BMI= weight/(height/100)**2
st.success(f"Your Body mass index is: {BMI}")
st.subheader("Refer this chart and check to know your body condition !!")
#Adding image 
st.image('BMI-IMAGE.jpg')


