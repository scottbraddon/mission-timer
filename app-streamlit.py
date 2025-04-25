# mission_timer.py
import streamlit as st
import time
from datetime import timedelta
import uuid

# Page setup
st.set_page_config(page_title="⏲️ Mission Timer", layout="centered")
st.title("⏲️ Mission Timer")

# Helper to format seconds as H:MM:SS
def format_time(seconds: float) -> str:
    return str(timedelta(seconds=int(seconds)))

# Initialize session state for timers
if "timers" not in st.session_state:
    st.session_state.timers = {}

# UI: Create a new timer
st.subheader("Create a New Mission Timer")
new_h = st.number_input("Hours", min_value=0, max_value=99, value=0, key="new_h")
new_m = st.number_input("Minutes", min_value=0, max_value=59, value=0, key="new_m")
new_s = st.number_input("Seconds", min_value=0, max_value=59, value=0, key="new_s")
new_name = st.text_input("Mission Name", f"Mission {len(st.session_state.timers)+1}", key="new_name")

if st.button("Add Timer", key="add_timer"):
    total_sec = new_h * 3600 + new_m * 60 + new_s
    if total_sec > 0:
        tid = str(uuid.uuid4())
        st.session_state.timers[tid] = {
            "name": new_name,
            "total": total_sec,
            "remaining": total_sec,
            "running": False,
            "last_update": None,
            "checkpoints": []
        }
        # Reset input fields
        st.session_state.new_h = 0
        st.session_state.new_m = 0
        st.session_state.new_s = 0
        st.session_state.new_name = f"Mission {len(st.session_state.timers)+1}"

# Display and update each timer
for tid, timer in st.session_state.timers.items():
    # Update remaining time if running
    if timer["running"]:
        now = time.time()
        last = timer.get("last_update", now)
        elapsed = now - last
        timer["remaining"] = max(0, timer["remaining"] - elapsed)
        timer["last_update"] = now
        if timer["remaining"] <= 0:
            timer["running"] = False
            timer["remaining"] = 0

    st.markdown(f"### ⏱️ {timer['name']}")
    c1, c2, c3 = st.columns(3)
    c1.metric("Remaining", format_time(timer["remaining"]))

    # Start / Pause
    if not timer["running"]:
        if c2.button("▶️ Start", key=f"start_{tid}"):
            timer["running"] = True
            timer["last_update"] = time.time()
    else:
        if c2.button("⏸️ Pause", key=f"pause_{tid}"):
            timer["running"] = False

    # Reset
    if c3.button("🔁 Reset", key=f"reset_{tid}"):
        timer["running"] = False
        timer["remaining"] = timer["total"]
        timer["last_update"] = None

    # Checkpoints
    st.markdown("#### 📍 Checkpoints")
    for cp in timer["checkpoints"]:
        st.write(f"- {cp['label']} at {format_time(cp['at'])}")

    # Add a new checkpoint
    cp1, cp2, cp3, cp4 = st.columns([1, 1, 1, 3])
    ch = cp1.number_input("H", min_value=0, value=0, key=f"ch_{tid}")
    cm = cp2.number_input("M", min_value=0, max_value=59, value=0, key=f"cm_{tid}")
    cs = cp3.number_input("S", min_value=0, max_value=59, value=0, key=f"cs_{tid}")
    label = cp4.text_input("Label", value="", key=f"label_{tid}")
    if cp4.button("Add Checkpoint", key=f"addcp_{tid}"):
        at_sec = ch * 3600 + cm * 60 + cs
        if 0 < at_sec < timer["total"]:
            timer["checkpoints"].append({
                "at": at_sec,
                "label": label or format_time(at_sec)
            })
            # Reset checkpoint inputs
            st.session_state[f"ch_{tid}"] = 0
            st.session_state[f"cm_{tid}"] = 0
            st.session_state[f"cs_{tid}"] = 0
            st.session_state[f"label_{tid}"] = ""
            st.experimental_rerun()

# Auto-rerun to update timers every second while any is running
if any(t["running"] for t in st.session_state.timers.values()):
    time.sleep(1)
    st.experimental_rerun()
