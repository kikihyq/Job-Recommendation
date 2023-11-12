# -*- coding: utf-8 -*-
"""IT5006_Streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NKt-O17LVxk2Yep3aPCMO3a0BWeyZqc9

# Streamlit
"""

# pip install streamlit

# import os
# print(os.getcwd())

# import sys
# sys.path.append('/content/drive/MyDrive/IT5006')
# from data_processing import combine_datasets, dummy_to_col, visualize_survey_data

import streamlit as st

# disable showPyplotGlobalUse warning 
st.set_option('deprecation.showPyplotGlobalUse', False)

intro_text = '''**Exploring the Gender Pay Gap in the Tech Industry: A Data Analytics Investigation**

In an era of progress and inclusivity, it is imperative to address disparities that persist in various professional domains. Our data analytics project embarks on a comprehensive examination of the gender pay gap within the tech industry. Through rigorous analysis of a Kaggle survey dataset, we aim to uncover the multifaceted factors that contribute to income inequality between men and women.

Our investigation begins with a meticulous time series analysis, charting the evolution of median salaries across different regions and education levels from 2020 to 2022. Our primary objective is to discern if there have been changes in gender-based pay disparities within these temporal shifts.

Furthermore, we scrutinize the intricate interplay between salary and gender, dissecting it by various aspects of qualification.  This nuanced examination aims to shed light on the reasons behind the pay gap in this field and explore any potential connections to qualifications.


Our journey through this data analytics project not only seeks to quantify the gender pay gap but also to uncover the underlying dynamics that perpetuate this inequality. By doing so, we hope to contribute to the ongoing dialogue on gender equity in the workplace and pave the way for informed decisions that promote fairness and inclusivity.'''


# Define Streamlit app
st.header("Interactive Survey Data Visualization")

st.markdown(intro_text)


# !pip install streamlit

# !pip install pyngrok
# from pyngrok import ngrok

# # deploy Streamlit  on web 
# public_url = ngrok.connect(port='8501')
# public_url

# !streamlit run /content/drive/MyDrive/IT5006/data_streamlit.py