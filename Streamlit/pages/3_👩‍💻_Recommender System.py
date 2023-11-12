import streamlit as st


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





page_title_dict = {
    'highest_edu_lv': 'Highest Level of Education',
    'age' : 'Age',
    'year_of_coding': 'Year of Coding',
    'year_of_ml': 'Year of Doing Machine Learning',
    # 'role_title': 'Role Title',
    'program_language': 'Programming Language',
    'role_activity': 'Role Activity',
    'machine_learning_lib': 'Machine Learning Library'
    # 'region': 'Region',
    # 'all': 'these 3 years'
}

education = {


}

# 在侧边栏创建一个 multiselect
selected_feature = st.sidebar.multiselect("Select Feature", list(page_title_dict.values()))
num_recommendation = st.sidebar.number_input("Number of Recommendation",value=0, step=1,max_value=5,min_value=0)

# 根据用户选择的内容，在主页面上动态创建相应数量的 selectbox
for option in selected_feature:
    if option =='Highest Level of Education':
        selected_education = st.selectbox(f"{option}", ["Bachelor", "Master", "Doctoral",'Others'], placeholder="Choose an option")
    if option=='Age':
        selected_age = st.selectbox(f"{option}", ['18-21','22-24','25-29','30-34','35-40','20-50','50-60'])
    if option == 'Year of Coding':
        selected_ycoding = st.number_input(f"{option}", value=0,step=1,min_value=0,max_value=60)
    if option == 'Year of Doing Machine Learning':
        selected_yml = st.selectbox(f"{option}", [0,1,2,3,4,5,10,20,30])
    if option =='Programming Language':
        selected_language = st.multiselect(f"{option}", ['Python','SQL','R','C','Java'])
    if option =='Role Activity':
        selected_activity = st.multiselect(f"{option}", ['Analyze Data','Build ML prototypes','RDo ML Research','Other'])
    if option =='Machine Learning Library':
        selected_library = st.multiselect(f"{option}", ['SKlearn','Tensorflow','Keras','Pytorch','XGBoost','Other'])
    # st.write(f"你在 {option} 中选择的子选项是:", selected_value)
    st.write(" ")
if selected_feature:   
    if st.button('Recommend'):
        st.write(f"### Your Top {num_recommendation} Recommendations:")