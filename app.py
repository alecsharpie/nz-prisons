import streamlit as st
import streamlit.components.v1 as components
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import pandas as pd

from streamlit_pages.streamlit_pages import MultiPage
from graphs.create_graphs \
    import rate_graph, drugs_graph, demo_graph, conv_rate_graph, staff_graph, reimprisonment_graph

st.set_page_config(
    page_title="NZ's Prisons",
    page_icon="🔑",
    layout="wide")

def home():

    st.markdown( """---""")

    st.markdown("""
                There are 18 Prisons in New Zealand.

                One prison, Auckland South Corrections Facility (Kohuora), is privately run by Serco. They manage over 500 prisons internationally. <a href="#ref2"><i>[2]</i></a> <br> <br>
                The other 17 are run by NZ Government's Department of Corrections. <a href="#ref3"><i>[3]</i></a>

                """,
                unsafe_allow_html=True)

    st.markdown("""---""")

    st.markdown("""Quick Glossary""")

    st.markdown("""
                <b>Charged</b> - Someone accused of an offence.
                <br>
                <b>Convicted</b> - Someone Declared guilty of an offence.
                """,
                unsafe_allow_html=True)

    st.markdown("""---""")

    st.markdown('''
                ### Number of prisoners per Capita
                ''')
    rate = st.columns([2, 1])

    rate[0].pyplot(rate_graph())

    rate[1].write("""
        If you line up all the countries by number of prisoners per capita, NZ is 61st from the top.
        To help visualize its position, imagine countries in 3 equal sized groups,
        New Zealand's group imprisons people at the highest rate.
        <a href="#ref4"><i>[4]</i></a> <a href="#ref5"><i>[5]</i></a>
        """)
    rate[1].write("""
        The USA has the highest imprisonment rate, while Guinea-Bissau has the lowest. <a href="#ref4"><i>[4]</i></a>
                  """)
    st.markdown("""---""")

    st.markdown('''
                ### Demographics
                ''')
    demo = st.columns([2, 1])

    demo[0].pyplot(demo_graph())

    demo[1].markdown("""
        Thankfully the proportion of young people being convicted of crimes has dropped significantly in the last 15 years. <a href="#ref1"><i>[1]</i></a>
        """)

    demo[1].markdown("""
        <br>
        <br>
        Men have always made up 80-90 percent of prisoners. <a href="#ref1"><i>[1]</i></a>
        """,
                     unsafe_allow_html=True)

    demo[1].markdown("""
        <br>
        <br>
        The proportion of convictions of Maori people has been increaing steadily for 40 years. <a href="#ref1"><i>[1]</i></a>
        """,
                     unsafe_allow_html=True)
    st.markdown('---')

    st.markdown('''
                ### Conviction rate inequality
                ''')
    demo = st.columns([2, 1])

    demo[0].pyplot(conv_rate_graph())

    demo[1].markdown("""
        Conviction rate is the percentage of people who have been convicted of the crime they were charged with. <br>
        For the last 30 years Maori have had a higher conviction rate than any other ethnic group. <a href="#ref1"><i>[1]</i></a>
        """,
                     unsafe_allow_html=True)

    demo[1].markdown("""
        Maori people account for 53% of NZ's prisoners but only 17% of national population. <a href="#ref6"><i>[6]</i></a> <a href="#ref7"><i>[7]</i></a>
        This means 1 in 174 Maori in NZ are in prison, compared with 1 in 996 Non-Maori, and 1 in 1300 Pakeha.
        """,
                     unsafe_allow_html=True)

    demo[1].markdown("""
        Asian people have a much lower conviction rate than any other ethnicity.<a href="#ref1"><i>[1]</i></a>
        """,
                     unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('''
                ### Drug Offences
                ''')
    drugs = st.columns([2, 1])
    drugs[0].pyplot(drugs_graph())
    drugs[1].write("""
        Cannabis and Meth are by far the biggest contributors to drug convictions in NZ.
        Multiple studies show Methamphetamine causing ~3x as much harm to self than Cannabis.
        <a href="#ref1"><i>[1]</i></a> <a href="#ref8"><i>[8]</i></a> <a href="#ref9"><i>[9]</i></a>
        """)
    st.markdown("""---""")

    st.markdown('''
                ### Costs
                ''')
    st.markdown("""One Prisoner""")
    col1, col2, col3 = st.columns(3)
    col1.metric("Daily", "$385")
    col2.metric("Yearly", "$140,525")
    col3.metric("Avg Length Sentence", "$210,980")
    st.markdown(
        """All Prisoners (based on a 6258 prisoner avg)<a href="#ref3"><i>[3]</i></a>"""
    )
    col1_all, col2_all = st.columns([1, 2])
    col1_all.metric("Daily", "$2,409,330")
    col2_all.metric("Yearly", "$879,405,450")

    st.markdown("""
                <a href="#ref1"><i>[1]</i></a>
                """,
                unsafe_allow_html=True)
    st.markdown('---')

    st.markdown('''
                ### Staff
                ''')
    demo = st.columns([2, 1])

    demo[0].pyplot(staff_graph())

    demo[1].markdown("""
                Having prisoners is expensive, we employ 6400 staff to hold 8400 people captive in prison. <a href="#ref3"><i>[3]</i></a>

        """)

    st.markdown("---")

    st.markdown('''
                ### Re-imprisonment
                ''')
    demo = st.columns([2, 1])

    demo[0].pyplot(reimprisonment_graph())

    demo[1].markdown("""
                The longer you stay in prisons the less likely you are to be reimprisoned. People who go to prison for less than 6 months have almost the same odds as a coin flip of going back to prison.
                The rate of prisoners pursuing and acheiving skill certificates is low with only 0.6% people in prison <a href="#ref3"><i>[3]</i></a>
                The average length prison sentence is 1.5 years.
        """)

    st.markdown("---")
    st.markdown("""
                Click <a href="#nz-s-prisons">here</a> to go back up to the top of the page so you can check out the prisons directory.
                """,
                unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
                ## References
                """)

    st.markdown("""
                #### [ref1]
                NZ, Dept of Justice, Research & data <br>
                [https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/](https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref2]
                Serco, Information about Auckland South Corrections Facility (Kohuora). <br>
                [https://www.serco.com/aspac/sector-expertise/justice/information-for-friends-and-family/auckland-south-corrections-facility](https://www.serco.com/aspac/sector-expertise/justice/information-for-friends-and-family/auckland-south-corrections-facility)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref3]
                Dept of Corrections, Annual Report, 1 July 2019 – 30 June 2020 <br>
                [https://www.corrections.govt.nz/resources/strategic_reports/annual-reports/annual_report_2019_2020](https://www.corrections.govt.nz/resources/strategic_reports/annual-reports/annual_report_2019_2020)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref4]
                Our World in Data, Incarceration rate in different countries, Dataset <br>
                [https://ourworldindata.org/grapher/prison-population-rate](https://ourworldindata.org/grapher/prison-population-rate)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref5]
                Our World in Data, Countries and their continents, Dataset <br>
                [https://ourworldindata.org/world-region-map-definitions](https://ourworldindata.org/world-region-map-definitions)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref6]
                Dpet of Corrections, Prison stats June 2021 <br>
                [https://www.corrections.govt.nz/resources/statistics/quarterly_prison_statistics/prison_stats_june_2021#ethnicity](https://www.corrections.govt.nz/resources/statistics/quarterly_prison_statistics/prison_stats_june_2021#ethnicity)

                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref7]
                Wikipedia, Demographics of New Zealand <br>
                [https://en.wikipedia.org/wiki/Demographics_of_New_Zealand](https://en.wikipedia.org/wiki/Demographics_of_New_Zealand)
                """,
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref8]
                Bonomo, Y. et al. “The Australian drug harms ranking study.” Journal of Psychopharmacology 33 (2019): 759 - 768. <br>
                [https://www.semanticscholar.org/paper/The-Australian-drug-harms-ranking-study-Bonomo-Norman/dd362c87c7340d759c8d114ea6b64232dcff9a71](https://www.semanticscholar.org/paper/The-Australian-drug-harms-ranking-study-Bonomo-Norman/dd362c87c7340d759c8d114ea6b64232dcff9a71)""",
                unsafe_allow_html=True)

    st.markdown("""
                #### [ref9]
                Nutt, David J., Leslie A. King, and Lawrence D. Phillips. "Drug harms in the UK: a multicriteria decision analysis." The Lancet 376.9752 (2010): 1558-1565. <br>
                [https://www.sciencedirect.com/science/article/pii/S0140673610614626?casa_token=Jcs457yUpbgAAAAA:xklnbRrus2NVRzlUBibsYXh_FdbE1RijoWCLSZsekJx-TeL8_UCI1geeP035TOyqkVTeze86Eps](https://www.sciencedirect.com/science/article/pii/S0140673610614626?casa_token=Jcs457yUpbgAAAAA:xklnbRrus2NVRzlUBibsYXh_FdbE1RijoWCLSZsekJx-TeL8_UCI1geeP035TOyqkVTeze86Eps)
                """,
                unsafe_allow_html=True)

    st.markdown("""---""")

    st.markdown("""
            Created by [Alec Sharp](https://www.alecsharpie.me/), October 2021.
            """,
            unsafe_allow_html=True)




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
    st.markdown("""
            Click <a href="#nz-s-prisons">here</a> to go back up to the top of the page so you can check out the prisons directory.
            """,
            unsafe_allow_html=True)

    st.markdown("""---""")

    st.markdown("""
        Created by [Alec Sharp](https://www.alecsharpie.me/), October 2021.
        """,
        unsafe_allow_html=True)

# call app class object
app = MultiPage()
# Add pages
app.add_page("Home", home)
app.add_page("Prisons List", prisons)
app.run()
