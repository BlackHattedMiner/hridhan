import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import webbrowser

st.title("Happy Birthday Hridhan!!")
st.header(" A Compilation of memories in Hridhan's Journal.")




email = 'https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=shreya24sep@gmail.com'

if st.sidebar.button('Contact me'):
    webbrowser.open_new_tab(email)

school = 'https://www.bkbirlaschoolkalyan.com/'

if st.sidebar.button('My Present School'):
    webbrowser.open_new_tab(school)

st.markdown("""
<style>
body {
    color: #00000;
}
</style>
    """, unsafe_allow_html=True)
page_bg_img = '''
<style>
body {
background-image: url("https://www.thewowstyle.com/wp-content/uploads/2015/07/natural-beach-pictures-.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


o = st.selectbox(
    'What Do You Want to know',
    ('Birth', 'Favourite Things', 'Milestones', 'Family', 'First Home', 'First Birthday', 'First School', 'Second Birthday', 'Second Home', 'Third Birthday', 'Second School', 'Ambitions')
)

if o == "Birth":
    st.success("I was born on 19th November 2016 to my parents Mr. Mahendra Pratap Singh and Shreya Singh at Astha Hospital, Kalyan, Maharashtra.")
    imga = Image.open("birth.jpeg")
    st.image(imga,width=500)
if o == "Favourite Things":
    st.success("Originally I am a very diligent and peaceful boy, but still I love mobile phones a lot :) xD")
    imgb = Image.open("fav.jpeg")
    st.image(imgb,width=500)
if o == "Milestones":
    st.success("Some of the milestones of my life till now are:")
    st.success("First Walk in 8 months")
    st.success("First Food: Cerelac")
    st.success("First Best Friend: Max the Teddy")
    imgc = Image.open("Walk.jpeg")
    st.image(imgc,width=500)
if o == "Family":
    st.success("I have a very vast and beautiful family which would take days to count, but the closest to me [in living beings] are my parents..")
    imgd = Image.open("fam.jpeg")
    imgr = Image.open("max.jpeg")
    st.image(imgd,width=450)
    st.image(imgr,width=450)
if o == "First Home":
    st.success("I was raised primarily at C5/77, CR Colony. It was a very beautiful place and I have a lot of mischivous memories bound to that place.....")
    imge = Image.open("fh.jpeg")
    st.image(imge,width=500)
if o == "First Birthday":
    st.success("On 19th November 2017 I celebrated my First Birthday at CR Club with full zeal and excitement.")
    imgf = Image.open("fb.jpeg")
    st.image(imgf,width=500)
if o == "Second Birthday":
    st.success("On 19th November I celebrated my second birthday at C5 Terrace.")
    imgz = Image.open("2.jpeg")
    st.image(imgz,width=500)
if o == "Second Home":
    st.success("I shifted with my family to C-11-176 CR colony in 2019. It is also a beautiful place and I love to live there too with my parents. :)")
    imgg = Image.open("nh.jpeg")
    st.image(imgg,width=500)
if o == "Third Birthday":
    st.success("On 19th November 2019 I celebrated my Third Birthday")
    imgh = Image.open("th.jpeg")
    st.image(imgh,width=500)
if o == "First School":
    st.success("I went to the school Bal Mandir in the early years. It was no more than 10 mnutes of my home, and my favourite days there were Birthday [Not Mine but of other students :D]")
    imgi = Image.open("fs.jpeg")
    st.image(imgi,width=500)    
if o == "Second School":
    st.success("I got my admission in BK Birla School in 2019, but poor me, I could not even attend school for one single day due to Covid-19, and now I have to have all my classes virtually..  :(")
    imgj = Image.open("class.jpeg")
    st.image(imgj,width=500)
if o == "Ambitions":
    st.success("I want to become an Astronaut.")
    st.success("I want to buy a pistol.....")
    st.success("I want to make a spaceship")
    imgk = Image.open("photofunny.net_.jpg")
    st.image(imgk,width=600)



