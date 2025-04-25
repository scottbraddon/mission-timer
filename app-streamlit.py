import streamlit as st
import time, datetime

def seconds_left():
    """Return seconds remaining or 0 if finished"""
    if "end_time" not in st.session_state:
        return 0
    return max(0, int(st.session_state.end_time - time.time()))

# ── UI ─────────────────────────────────────────────────────
hours   = st.number_input("Hours",   min_value=0, value=0)
minutes = st.number_input("Minutes", min_value=0, value=0)
seconds = st.number_input("Seconds", min_value=0, value=0)

if st.button("Start Timer"):
    total = int(hours)*3600 + int(minutes)*60 + int(seconds)
    if total <= 0:
        st.error("Please enter a duration greater than zero.")
    else:
        st.session_state.end_time = time.time() + total
        st.session_state.running  = True
        st.experimental_rerun()          # kick off the first refresh

# ── Countdown display ─────────────────────────────────────
if st.session_state.get("running", False):
    remaining = seconds_left()
    hrs, rem  = divmod(remaining, 3600)
    mins, secs = divmod(rem, 60)
    st.markdown(f"### ⏳ {hrs:02d}:{mins:02d}:{secs:02d}")
    if remaining > 0:
        time.sleep(1)
        st.experimental_rerun()
    else:
        st.success("⏰ **Time's up!**")
        st.session_state.running = False
