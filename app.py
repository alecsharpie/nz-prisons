import streamlit as st
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

images = os.listdir('images')


#fig, ax = plt.subplots()


#ax.imshow(face, cmap='gray')

size_list = []
for idx, img in enumerate(images):
    if img != '.DS_Store':
        prison_img = mpimg.imread('images/' + img)
        size_list.append(prison_img.shape)

mean_height = np.mean([size[0] for size in size_list])

height_changes = [(size[0] - mean_height) / size[0] for size in size_list]

new_widths = [
    (size[0][1] + (size[0][1] * size[1])) / 5
    for size in zip(size_list, height_changes)
]

for idx, img in enumerate(images[:10]):
    if img != '.DS_Store':
        prison_img = mpimg.imread('images/' + img)
        st.image('images/' + img, width = 300)


#for idx, img in enumerate(images[:3]):
#    prison_img = mpimg.imread('images/' + img)
#    fig, ax = plt.subplots(figsize=(4, ))
#    ax.axis('off')
#   ax.imshow(prison_img, interpolation="nearest")
#    fig.tight_layout()
#    st.pyplot(fig)
