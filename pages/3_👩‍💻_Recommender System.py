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
    'age' : 'Age',
    'highest_edu_lv': 'Highest Level of Education',
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
    if option=='Age':
        selected_age = st.number_input(f"{option}",min_value=18,step=1)
        if selected_age in range(18,22):
            age = 21
        elif selected_age in range(22,25):
            age = 24
        elif selected_age in range(25,30):
            age = 29
        elif selected_age in range(30,35):
            age = 24
        elif selected_age in range(35,40):
            age = 39
        elif selected_age in range(40,45):
            age = 44
        elif selected_age in range(45,50):
            age = 49
        elif selected_age in range(50,55):
            age = 54
        elif selected_age in range(55,60):
            age = 59
        elif selected_age in range(60,70):
            age = 69
        elif selected_age >=70:
            age = 70

    if option =='Highest Level of Education':
        selected_education = st.selectbox(f"{option}", ["Bachelor", "Master", "Doctoral",'Others'], placeholder="Choose an option")
        if selected_education=='Bachelor':
            highest_edu_lv_1 = 1
            highest_edu_lv_2=0
            highest_edu_lv_3=0
            highest_edu_lv_Other=0
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