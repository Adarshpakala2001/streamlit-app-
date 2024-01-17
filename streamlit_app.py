import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Title - it is used to add the title of an app
st.title("Basic Streamlit App")

# Header
st.header("Machine Learning")
st.write("This is a basic Streamlit app showcasing various functions and widgets.")

# sub header
st.subheader("Linear Regression")
st.text("This is a simple text.")

#st Info
st.info("Information details of a user")

# Warning message
st.warning("come on time or else you will be marked as absent")

# Error message
st.error("Wrong Password")

# Sucess Message
st.success("Congrats you have got A Grade")

# write 
st.write("employee name")
st.write(range(50))


# Markdown
st.subheader("Markdown")
st.markdown("You can use **Markdown** to format text.")

# Line Break
st.subheader("Line Break")
st.write("This is some text.")
st.write("This is more text with a line break.\nAnd another line break.")

# Data Frame
st.subheader("Data Frame")
data = {'Column 1': [1, 2, 3, 4],
        'Column 2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
st.dataframe(df)

# Table
st.subheader("Table")
st.table(df)

# Plotting
st.subheader("Plotting")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# Interactive Widgets
st.subheader("Interactive Widgets")

# Slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Selected value:", slider_value)

# Checkbox
checkbox_result = st.checkbox("Show plot")
if checkbox_result:
    st.line_chart(pd.DataFrame({'x': x, 'y': y}))

# Radio Buttons
radio_button_result = st.radio("Select one option", ["Option 1", "Option 2", "Option 3"])
st.write("Selected option:", radio_button_result)

# Selectbox
selectbox_result = st.selectbox("Select an item", ["Item 1", "Item 2", "Item 3"])
st.write("Selected item:", selectbox_result)

# Text Input
text_input_result = st.text_input("Enter some text", "Default Text")
st.write("Entered text:", text_input_result)

# Button
if st.button("Click me"):
    st.success("Button clicked!")

# Expander
with st.expander("Click to expand"):
    st.write("This is hidden by default and can be expanded.")

# Sidebars
st.sidebar.header("Sidebar")
st.sidebar.subheader("Sidebar Section")
st.sidebar.text("This is a sidebar.")

# Show Help Tooltip
st.help(st.button)

# File Upload
st.subheader("File Upload")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Raw Code
st.subheader("Raw Code")
st.code("""
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
""", language="python")
