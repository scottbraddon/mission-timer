import streamlit as st

st.title("⏰ Mission Timer")

# Inputs
a = st.number_input("First number", value=0.0, format="%.f", step=1.0)
b = st.number_input("Second number", value=0.0, format="%.f", step=1.0)

# Multiply button
if st.button("Multiply"):
    product = a * b
    st.success(f"Result: {product}")

# Create a Timer
st.subheader("Create a Countdown Timer")
hours = st.number_input("Hours", min_value=0, max_value=23, value=0, step=1)
minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0, step=1)
seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0, step=1)

if st.button("Start Timer"):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    if total_seconds <= 0:
        st.error("Please enter a duration greater than zero.")
    else:
        placeholder = st.empty()
        for remaining in range(total_seconds, -1, -1):
            hrs, rem = divmod(remaining, 3600)
            mins, secs = divmod(rem, 60)
            placeholder.markdown(f"**Time Remaining:** {hrs:02d}:{mins:02d}:{secs:02d}")
            time.sleep(1)
        placeholder.markdown("⏰ **Time's up!**")
