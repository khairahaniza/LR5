import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation Function")

st.title("Sigmoid Activation Function")
st.write("Sigmoid squashes input values into a range between 0 and 1.")

# Define Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate input values
x = np.linspace(-10, 10, 400)
y = sigmoid(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Activation Function")
ax.grid(True)

st.pyplot(fig)
