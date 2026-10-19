
from importlib import import_module

st = import_module("streamlit")

st.title("Project 02 - Test")
st.success("Streamlit is working!")

st.write("Number Guessing Game & Word Counter")

if st.button("Test button"):
    st.balloons()
    st.write("The button works!")
