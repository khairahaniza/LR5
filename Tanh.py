import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation Function")

st.title("Hyperbolic Tangent (Tanh)")
st.write("Tanh maps input values to a range between -1 and 1.")

# Define Tanh function
def tanh(x):
    return np.tanh(x)

# Generate input values
x = np.linspace(-10, 10, 400)
y = tanh(x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Tanh Activation Function")
ax.grid(True)

st.pyplot(fig)
