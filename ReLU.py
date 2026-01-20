import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation Function")

st.title("Rectified Linear Unit (ReLU)")
st.write("ReLU outputs the input directly if it is positive; otherwise, it outputs zero.")

def relu(x):
    return np.maximum(0, x)

x = np.linspace(-10, 10, 400)
y = relu(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("ReLU Activation Function")
ax.grid(True)

st.pyplot(fig)
