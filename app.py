import streamlit as st
import streamlit.components.v1 as components
import os
from streamlit_pages.streamlit_pages import MultiPage

st.set_page_config(
    page_title="NZ's Prisons",
    page_icon="🔑",
    layout="wide",  # wide
    initial_sidebar_state="auto")



def home():
    st.write("Welcome to home page")
    if st.button("Click Home"):
        st.write("Welcome to home page")


def about():
    st.write("Welcome to about page")
    if st.button("Click about"):
        st.write("Welcome to About page")


def contact():
    st.write("Welcome to contact page")
    if st.button("Click Contact"):
        st.write("Welcome to contact page")


# call app class object
app = MultiPage()
# Add pages
app.add_page("Home",home)
app.add_page("About",about)
app.add_page("Contact",contact)
app.run()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import pandas as pd


prisons_df = pd.read_csv('data/NZ_Prisons_Master.csv')

images = os.listdir('images')

images = [img for img in images if img != '.DS_Store']

st.header("NZ's Prisons - Our Prisons")

controls = st.columns(4)

region = controls[0].radio('Select a Region',
                              ('All', 'Northern','Central','Lower North','Southern'))
if region != 'All':
    prisons_df = prisons_df[prisons_df['region'] == region]

security = controls[1].radio(
    'Select a Security Level',
    ('All', 'Low-Medium', 'High', 'Maximum'))
if security != 'All':
    prisons_df = prisons_df[prisons_df['max_security'] == security]

order = controls[3].radio('Order by',
                             ('Total_Prisoners', 'Opened', 'Staff', 'Escape', 'Contraband'))

prisons_df = prisons_df.sort_values(order.lower())

components.html(
    """<hr style="height:10px;border:none;color:#C70039;background-color:#C70039;" /> """
)

for idx, row in prisons_df.iterrows():
    st.markdown(f"""
                ## {row['prison']}""")

    st.markdown(f"""
                [Website]({row['link']})  -
                {row['address']}  -
                {row['phone']}""")

    columns = st.columns(2)

    columns[0].image('images/' + row['image'], width=300)
    columns[0].write(f"Established: {row['opened']}")
    columns[0].write(f"{row['beds']} Bed's and {row['staff']} Staff")

    columns[1].markdown(f"""
                        {row['total_prisoners']} {row['gender']} Prisoners\n
                        Security: {row['max_security']}\n\n

                        Avg Incidents per year:\n
                        {row['escapes']} Escapes\n
                        {row['deaths']} Deaths\n
                        {row['contraband']} Contraband Items
                        """)
    components.html(
        """<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """
    )
