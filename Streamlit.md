# Open Streamlit
1. open Anaconda
2. choose the environment "finpy"
3. open terminal
4. 切换到streamlit.py的文件路径
4.1 `cd ..`  切换后到C:\Users>
        （Anaconda Prompt在默认路径下，无法直接cd到其他盘。只能在根目录下进行切换盘符。）
4.2 `cd..` 切换后到C:\>
4.3 `E:`  切换后到E:\>
4.4 `cd "E:\23Fall\NUS\Course\IT5006\Streamlit\"` 
     切换后到目标文件夹：E:\23Fall\NUS\Course\IT5006\Streamlit\中
5. 运行目标代码文件`streamlit run streamlit_app.py`

Then Streamlit's Hello app should appear in a new tab in your web browser!

---
# St.button
st.button allows the display of a button widget.
## What we are building
a simple app that performs conditionally prints out messages depending on the button was pressed or not

Flow of the app:

1. By default, the app prints `Goodbye`
2. Upon clicking on the button, the app displays the alternative message `Why hello there`

## Code
```python
import streamlit as st
st.header("st.button")   # create a header text for the app

if st.button("Say hello"):  # st.button accepts the label "Say Hello"
    st.write("Why hello there")
else:
    st.write("Goodby")
``````
## Explanation
- `st.header("st.button") `  create a header text for the app
- `st.button()` command accepts the `label` input argument of `Say hello`, which is the text that the button displays
- `st.write()` is used to print text 
---
 
 # Day 4
 https://30days.streamlit.app/?challenge=Day4

 1. 切换目录，然后在"E:\23Fall\NUS\Course\IT5006\Sreamlit\" 里新建了一个环境：YT_dashboard_St   python=3.8
 2. `conda create -n YT_dashboard_St python=3.8`
 3. `conda activate YT_dashboard_St`
 4. `pip install streamlit`
 5. `pip install plotly`
---

# Day 5

## st.write
In addition to being able to display text, the following can also be displayed via the st.write() command:

Prints strings; works like `st.markdown()`
Displays a Python `dict`
Displays `pandas` DataFrame can be displayed as a table
Plots/graphs/figures from `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
And more :https://docs.streamlit.io/library/api-reference/write-magic/st.write

## What we're building?
A simple app showing the various ways on how to use the st.write() command for displaying text, numbers, DataFrames and plots.

## Explanation
- Example 1 : Its basic use case is to display text and Markdown-formatted text: `st.write('Hello, *World!* :sunglasses:')`     ' :sunglasses:'

- Example 2: As mentioned above, it can also be used to display other data formats such as numbers:
`st.write(1234)`

- Example 3 : DataFrames can also be displayed as follows:
```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
``````

- Example 4 : You can pass in multiple arguments:
`st.write('Below is a DataFrame:', df, 'Above is a dataframe.')`


- Example 5 Finally, you can also display plots as well by passing it to a variable as follows:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
``````

## Further reading
In addition to st.write, you can explore the other ways of displaying text:

- [st.markdown](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [st.header](https://docs.streamlit.io/library/api-reference/text/st.header)
- [st.subheader](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [st.caption](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [st.text](https://docs.streamlit.io/library/api-reference/text/st.text)
- [st.latex](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [st.code](https://docs.streamlit.io/library/api-reference/text/st.code)
---

***