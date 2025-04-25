import streamlit as st

st.title("Multiplier")

# Inputs
a = st.number_input("First number", value=0.0, format="%.f", step=1.0)
b = st.number_input("Second number", value=0.0, format="%.f", step=1.0)

# Multiply button
if st.button("Multiply"):
    product = a * b
    st.success(f"Result: {product}")
