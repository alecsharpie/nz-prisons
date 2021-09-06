import streamlit as st
import streamlit.components.v1 as components
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import pandas as pd

st.set_page_config(
    page_title="NZ's Prisons",  # => Quick reference - Streamlit
    page_icon="🔒",
    layout="centered",  # wide
    initial_sidebar_state="auto")

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




for idx, row in prisons_df.iterrows():
    st.markdown(f"""
                ## {row['prison']}""")

    columns = st.columns(2)

    columns[0].image('images/' + row['image'], width=300)
    #columns[0].write(prison_img)
    columns[1].markdown(f"""
                        {row['total_prisoners']} {row['gender']} Prisoners





                        Contact:
                        [Dept Corrections Website]({row['link']})
                        {row['address']}
                        {row['phone']}
                        """)
    #last_name = columns[1].text_input("Last name", value="Doe")
    #columns[1].write(last_name)

    #st.image('images/' + row['image'], width=300)

    components.html(
        """<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """
    )



#for idx, img in enumerate(images[:3]):
#    prison_img = mpimg.imread('images/' + img)
#    fig, ax = plt.subplots(figsize=(4, ))
#    ax.axis('off')
#   ax.imshow(prison_img, interpolation="nearest")
#    fig.tight_layout()
#    st.pyplot(fig)
