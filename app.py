import streamlit as st

st.set_page_config(
    page_title="Power Factor Calculator",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Power Factor Calculator")
st.write("BEEE Mini Project – Power Factor Visualization")

st.divider()

v = st.number_input("Enter Voltage (V)", min_value=0.0)
i = st.number_input("Enter Current (A)", min_value=0.0)
p = st.number_input("Enter Active Power (W)", min_value=0.0)

pf = None

if st.button("Calculate Power Factor"):
    if v > 0 and i > 0:
        pf = p / (v * i)
        st.success(f"Power Factor = {pf:.2f}")
    else:
        st.error("Voltage and Current must be greater than zero")

if pf is not None:
    st.subheader("📟 Power Factor Gauge")
    st.progress(min(pf, 1.0))

    if pf >= 0.95:
        st.success("🟢 Excellent Power Factor")
    elif pf >= 0.8:
        st.warning("🟡 Good Power Factor")
    else:
        st.error("🔴 Poor Power Factor")
