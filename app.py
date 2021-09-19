import streamlit as st
import streamlit.components.v1 as components
from streamlit_pages.streamlit_pages import MultiPage
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

import numpy as np
import pandas as pd

st.set_page_config(
    page_title="NZ's baddies",
    page_icon="🔑",
    layout="wide")


def home():

    conviction_count = pd.read_csv('data/drug_conviction_count.csv')

    st.write("We employ 6400 people to hold 8400 people captive")




    st.write("Drug Offences")
    drugs = st.columns([2, 1])

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.set_style("ticks")
    sns.set_palette('colorblind')
    sns.lineplot(data=conviction_count, hue='drug', x='year', y='count', ax = ax)
    plt.legend(title='Drug')
    plt.xlabel('Year')
    plt.ylabel('Number of Offences')
    sns.despine()
    drugs[0].pyplot(fig)
    drugs[1].write("""
        Cannabis and Meth are by far the biggest contributors to drug convictions in NZ.
        """)


def prisons():

    prisons_df = pd.read_csv('data/NZ_Prisons_Master.csv')

    to_convert_for_sort = ['escapes', 'deaths','contraband']

    for col in to_convert_for_sort:
        prisons_df[col] = prisons_df[col].str.replace('[^0-9]','')
        prisons_df[col] = pd.to_numeric(prisons_df[col], errors = 'coerce')

    images = os.listdir('images')

    images = [img for img in images if img != '.DS_Store']

    st.markdown("""---""")
    st.markdown("""View options:""")


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


    order = controls[3].radio(
        'Order by',
        ('Total_Prisoners', 'Opened', 'Staff', 'Escapes', 'Contraband'))

    prisons_df = prisons_df.sort_values(order.lower(), ascending = False)

    st.markdown("""---""")


    for idx, row in prisons_df.iterrows():
        st.markdown(f"""
                    ## {row['prison']}""")

        st.markdown(f"""
                    [Website]({row['link']})  -
                    {row['address']}  -
                    {row['phone']}""")
        st.write(f"Established: {row['opened']}")

        columns = st.columns(2)

        columns[0].image('images/' + row['image'], width=300)
        columns[1].write(
            f"{row['total_prisoners']} {row['gender']} Prisoners\n and {row['staff']} Staff"
        )

        columns[1].markdown(f"""
                            \n
                            Security: {row['max_security']}\n\n

                            Avg Incidents per year:\n
                            {row['escapes']} Escapes\n
                            {row['deaths']} Deaths\n
                            {row['contraband']} Contraband Items
                            """)
        st.markdown("""---""")


# call app class object
app = MultiPage()
# Add pages
app.add_page("Overview",home)
app.add_page("Our Prisons",prisons)
app.run()
