import streamlit as st
import pandas as pd
import numpy as np

# Part 1
# st.write("Hello World!")


# Part 2
# import streamlit as st
# st.header("st.button")   # create a header text for the app

# if st.button("Say hello"):
#     st.write("Why hello there")
# else:
#     st.write("Goodby")


# Part 5
# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write')

# # Example 1

# st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)



# # Test
# import streamlit as st
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = sns.load_dataset("tips")

# # 创建图形和轴
# fig, ax = plt.subplots()

# # 绘制Seaborn箱线图
# sns.boxplot(x="day", y="total_bill", data=data, ax=ax)

# # 显示图形
# st.pyplot(fig)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)