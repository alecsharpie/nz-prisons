import streamlit as st
import streamlit.components.v1 as components
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import pandas as pd

from streamlit_pages.streamlit_pages import MultiPage
from graphs.create_graphs import rate_graph, drugs_graph

st.set_page_config(
    page_title="NZ's Prisons",
    page_icon="🔑",
    layout="wide")


def home():
    st.write("whos in our prisons?")

    st.write("We employ 6400 people to hold 8400 people captive")

    st.write("Compared with other countries how packed are are prisons?")
    rate = st.columns([2, 1])

    rate[0].pyplot(rate_graph())

    rate[1].write("""

        """)


    st.write("Gender")





    st.write("Drug Offences")
    drugs = st.columns([2, 1])
    drugs[0].pyplot(drugs_graph())
    drugs[1].write("""
        Cannabis and Meth are by far the biggest contributors to drug convictions in NZ.
        Multiple studies show Methamphetamine causing ~3x as much harm to self than Cannabis.
        [ref1] [ref2]
        """)


def prisons():

    prisons_df = pd.read_csv('data/prisons_info.csv')

    to_convert_for_sort = ['escapes', 'deaths','contraband']

    #for col in to_convert_for_sort:
    #    prisons_df[col] = prisons_df[col].str.replace('[^0-9]','')
    #    prisons_df[col] = pd.to_numeric(prisons_df[col], errors = 'coerce', type = float)

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

    prisons_df = prisons_df.sort_values(order.lower(),
                                        ascending=False,
                                        na_position='first')

    st.markdown("""---""")



    for idx, row in prisons_df.iterrows():
        st.markdown(f"""
                    ## {row['prison']}""")

        st.markdown(f"""
                    [Website]({row['link']})  -
                    {row['address']}  -
                    {row['phone']}""")
        st.write(f"Established: {row['opened']}")

        columns = st.columns(3)

        columns[0].image('images/' + row['image'])
        columns[1].
        columns[2].write(
            f"{row['total_prisoners']} {row['gender']} Prisoners\n and {row['staff']} Staff"
        )
        columns[2].markdown(f"""
                            Security: {row['max_security']}
                            """)
        columns[2].markdown('Avg Incidents per year:')
        columns[2].markdown(
            f"""<p style="font-family:Sans-serif; color:#ffffff; font-size: 12px;">
                            🏃 Escapes: {row['escapes']}<br>
                            💀 Deaths {row['deaths']}<br>
                            💊 Contraband {row['contraband']}<br>
                            </p>
                            """,
            unsafe_allow_html=True)

        # df = pd.DataFrame({
        #     'Escapes': [row['escapes']],
        #     'Deaths': [row['deaths']],
        #     'Contraband': [row['contraband']]
        # })
        #df.style.format({
        #    "'Escapes'": "{:20,.0f}",
        #}).hide_index()
        #df.index = [""] * len(df)
        #st.table(df)
        #columns[1].dataframe(df)
        st.markdown("""---""")


# call app class object
app = MultiPage()
# Add pages
app.add_page("Prisoners",home)
app.add_page("Prisons",prisons)
app.run()
