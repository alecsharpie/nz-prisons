import streamlit as st
import streamlit.components.v1 as components
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import pandas as pd

from streamlit_pages.streamlit_pages import MultiPage
from graphs.create_graphs import rate_graph, drugs_graph, demo_graph

st.set_page_config(
    page_title="NZ's Prisons",
    page_icon="🔑",
    layout="wide")


def home():
    st.write("Who are our prisoners?")

    st.write("We employ 6400 people to hold 8400 people captive")
    st.markdown('''
                ### Demographics
                ''')
    demo = st.columns([2, 1])

    demo[0].pyplot(demo_graph())

    demo[1].write("""
        Thankfully the number of young people in prison have droppping significantly in the last 15 years. [ref1]
        """)

    demo[1].markdown("""
        <br>
        <br>
        Men have always made up 80-90 percent of prisoners. [ref1]
        """,
                     unsafe_allow_html=True)

    demo[1].markdown("""
        <br>
        <br>
        The proportion of convictions of Maori people has been increaing steadily for 40 years. [ref1]
        Maori people account for 53% of NZ's prisoners but only 17% of national population. [ref2] [ref3]

        1 in 174 Maori in NZ are in prison, compared with 1 in 996 Non-Maori, and 1 in 1300 Pakeha. [ref3]
        """,
                     unsafe_allow_html=True)

    st.markdown('''
                ### Prisoners per Capita
                ''')
    rate = st.columns([2, 1])

    rate[0].pyplot(rate_graph())

    rate[1].write("""
        If you line up all the countries by prisoners per capita, NZ is 61st from the top.
        To help visualize its position, imagine countries in 3 equal sized groups,
        New Zealand's group imprisons people at the highest rate.
        [ref4]
        """)
    rate[1].write("""
        The USA has the highest imprisonment rate, while Guinea-Bissau has the lowest. [ref4]
                  """)
    st.markdown("""---""")

    st.markdown('''
                ### Drug Offences
                ''')
    drugs = st.columns([2, 1])
    drugs[0].pyplot(drugs_graph())
    drugs[1].write("""
        Cannabis and Meth are by far the biggest contributors to drug convictions in NZ.
        Multiple studies show Methamphetamine causing ~3x as much harm to self than Cannabis.
        [ref1] [ref2]
        """)
    st.markdown("""---""")
    st.markdown("""
                ## References
                """)
    st.markdown("""
                #### [ref1]
                NZ, Dept of Justice, Research & data
                [https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/](https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/)
                """)
    st.markdown("""
                #### [ref2]


                """)
    st.markdown("""
                #### [ref3]


                """)


def prisons():

    prisons_df = pd.read_csv('data/prisons_info.csv')

    images = os.listdir('images')

    images = [img for img in images if img != '.DS_Store']

    st.markdown("""---""")
    st.markdown("""View options:""")


    controls = st.columns(4)

    region = controls[0].radio('Select a Region',
                                ('All','Upper North','Central North','Lower North','South'))
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

        columns = st.columns(3)

        columns[0].image('maps/' + row['image'])
        columns[1].image('images/' + row['image'])

        columns[2].markdown(
            f"""<p style="font-family:Sans-serif; color:#ffffff; font-size: 14px;">
                            {row['total_prisoners']} {row['gender']} Prisoners<br>
                            {row['staff']} Staff<br>
                            </p>
                            """,
            unsafe_allow_html=True)
        columns[2].markdown(
            f"""<p style="font-family:Sans-serif; color:#ffffff; font-size: 12px;">
                            🛡️ {row['max_security']} security<br>
                            <br>
                            🏃 {row['escapes']} avg escapes per year<br>
                            💀 {row['deaths']} avg deaths per year<br>
                            💊 {row['contraband']} avg contraband items per year<br>
                            </p>
                            """,
            unsafe_allow_html=True)
        columns[2].markdown(
            f"""<p style="font-family:Sans-serif; color:#ffffff; font-size: 14px;">
                            Established in {row['opened']}<br>
                            </p>
                            """,
            unsafe_allow_html=True)

        st.markdown("""---""")


def resources():
    pass


# call app class object
app = MultiPage()
# Add pages
app.add_page("Prisoners",home)
app.add_page("Prisons",prisons)
app.add_page("Resources", resources)
app.run()
