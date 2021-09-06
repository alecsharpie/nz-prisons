import streamlit as st
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




for idx, row in prisons_df.iterrows():
    st.markdown(f"""
                ## {row['prison']}""")
    st.image('images/' + row['image'], width=300)


#for idx, img in enumerate(images[:3]):
#    prison_img = mpimg.imread('images/' + img)
#    fig, ax = plt.subplots(figsize=(4, ))
#    ax.axis('off')
#   ax.imshow(prison_img, interpolation="nearest")
#    fig.tight_layout()
#    st.pyplot(fig)
