import streamlit as st

st.markdown("# 🎉欢迎来到黄韵淇设计的小游戏🎉")
st.sidebar.markdown("# 情景")

page_title_dict = {
    'highest_edu_lv': 'A',
    'year_of_coding': 'B',
    'role_title': 'C',
    'program_language': 'D',
    'role_activity': 'E'
    # 'all': 'these 3 years'
}


selected_feature = True
# 在侧边栏创建一个 multiselect
selected_feature = st.sidebar.selectbox("请任意选择一类，抽盲盒", ['','A','B','C','D','E'])
num_recommendation = st.sidebar.number_input("请选择你喜欢的数字,0-10",value=0, step=1,min_value=0,max_value=10)


if selected_feature:
    if st.button("开盲盒"):
        st.write(f"### 你的盲盒结果如下:")
        # 根据用户选择的内容，在主页面上动态创建相应数量的 selectbox
        for option in selected_feature:
            if option =='A':
                st.write("奖励亲亲一枚😘")
            elif option=='B':
                st.write("今天天气很好,我很想你🥰")
            elif option=='C':
                st.write('你个懒虫，快去给我学习！！！✍️')
            elif option=='D':
                st.write('恭喜你中终极大奖啦！！你需要请我喝一杯奶茶😁')
            elif option=='E':
                if st.button('再来一次'):
                    st.write("无")


