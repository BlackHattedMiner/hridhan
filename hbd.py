import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import webbrowser

st.title("Happy Birthday Hridhan!!")
st.header(" A Compilation of memories..")




email = 'https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=shreya24sep@gmail.com'

if st.sidebar.button('Contact me'):
    webbrowser.open_new_tab(email)

school = ''

if st.sidebar.button('My Present School'):
    webbrowser.open_new_tab(school)




o = st.selectbox(
    'Select State Name',
    ('Birth', 'Favourite Things', 'Favourite Foods', 'Milestones', 'Family', 'First Home', 'First Birthday', 'First School', 'Second Birthday', 'Second Home', 'Third Birthday', 'Second School')
)

if o == "Birth":
    st.success("")
if o == "Favourite Things":
    st.success("")
if o == "Milestones":
    st.success("")
if o == "Family":
    st.success("")
if o == "First Home":
    st.success("")
if o == "First Birthday":
    st.success("")
if o == "Second Birthday":
    st.success("")
if o == "Second Home":
    st.success("")
if o == "Third Birthday":
    st.success("")
if o == "First School":
    st.success("")
if o == "Second School":
    st.success("")





