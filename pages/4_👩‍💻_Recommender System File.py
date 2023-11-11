import streamlit as st
import pandas as pd
from io import StringIO


text = """
<div style="text-align: center;">
    <h1>Job Recommendation App</h1>
</div>
"""
st.markdown(text, unsafe_allow_html=True)


st.sidebar.markdown("# Job Recommendation 👩‍💻")

# Images
st.write(" ")
col1, col2 = st.columns(2)

with col1:
    st.image("2.svg")
    st.write(" ")
with col2:
    st.image("3.svg")




uploaded_file = st.file_uploader("Please Upload a File", type=["pdf", "txt", "docx"])

if uploaded_file is not None:
    st.write("You have uploaded the file: ", uploaded_file.name)

    # 处理上传的文档，例如读取内容等
    # content = uploaded_file.read()
    # 进一步的操作...