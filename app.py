import streamlit as st


fig, ax = plt.subplots()


ax.imshow(face, cmap='gray')

st.pyplot(fig)
