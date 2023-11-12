import streamlit as st
import pandas as pd
from openai import OpenAI

# Header
text = """
<div style="text-align: center;">
    <h1>Job Recommendation App</h1>
</div>
"""
st.markdown(text, unsafe_allow_html=True)


st.sidebar.markdown("# Job Recommendation 👩‍💻")
st.sidebar.write("Please choose your input type:")
# Images
st.write(" ")
col1, col2 = st.columns(2)

with col1:
    st.image("2.svg")
    st.write(" ")
with col2:
    st.image("3.svg")

def gpt_read_cv(cv):
        client = OpenAI(api_key='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')

        sys_prompt = '''
        Be a professional HR manager. You will receive a  candidate CV.
        You have to judge whether the candidate pose these skills.
        If you are not certain if the candidate pose that skill, write 0, otherwise write 1.
        Format your ouput as the table and fill in the table with the requirement.
        You need to fill all field.
        Only output the table, no need any explaination.
        For year calculation, today is 2023 Sept.

        Skill	Value
        Build Data Infrastructure	1: if have 0: if don't have
        Build Machine Learning Prototypes	1: if have 0: if don't have
        Build Machine Learning Service	1: if have 0: if don't have
        Machine Learning Research	1: if have 0: if don't have
        Python	1: if have 0: if don't have
        R	1: if have 0: if don't have
        SQL	1: if have 0: if don't have
        C	1: if have 0: if don't have
        C++	1: if have 0: if don't have
        Java	1: if have 0: if don't have
        JavaScript	1: if have 0: if don't have
        Julia	1: if have 0: if don't have
        Bash	1: if have 0: if don't have
        MATLAB	1: if have 0: if don't have
        Scikit-Learn	1: if have 0: if don't have
        TensorFlow	1: if have 0: if don't have
        Keras	1: if have 0: if don't have
        PyTorch	1: if have 0: if don't have
        Fastai	1: if have 0: if don't have
        XGBoost	1: if have 0: if don't have
        LightGBM	1: if have 0: if don't have
        CatBoost	1: if have 0: if don't have
        Caret	1: if have 0: if don't have
        Tidymodels	1: if have 0: if don't have
        JAX: if have 0: if don't have
        Regression   1: if have 0: if don't have
        decision tree, random forest  1: if have 0: if don't have
        gradient boosting (xgboost, lightgbm)  1: if have 0: if don't have
        Bayesian approach   1: if have 0: if don't have
        Evolutionary approach 1: if have 0: if don't have
        Dense Neural Network 1: if have 0: if don't have
        Convolutional Neural Network 1: if have 0: if don't have
        Generative Adversarial Network 1: if have 0: if don't have
        Recurrent Neural Network 1: if have 0: if don't have
        Transformer Networks (BERT, gpt-3, etc) 1: if have 0: if don't have
        highest obtained education level	categorical: [Bachelor Degree / Master Degree /  Doctor Degree, Other]
        machine learning year of experience 	year, int
        coding year of experience	year, int

        Output format:

        field: value, field2: value2 ...
        '''

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": sys_prompt,
                },
                {
                    "role": "user",
                    "content": cv,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content


option_select = st.sidebar.checkbox('Select Feature')
option_txt = st.sidebar.checkbox('Input Text')
num_recommendation = st.sidebar.number_input("Number of Recommendation",value=0, step=1,max_value=5,min_value=0)
if option_txt:
    # Text Input    
    st.markdown("### Please enter your profile👇")
    profile = st.text_area(label="")
    if profile is None:
        st.write("Please input your profile")
    else :
        response = gpt_read_cv(profile)
        st.write(response)
        if st.button('Recommend'):
            st.write(f"### Your Top {num_recommendation} Recommendations:")    


# Feature Select
if option_select:
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