import streamlit as st
from model import predict_risk

# Page config
st.set_page_config(page_title="AI Risk Predictor", layout="centered")

# Title
st.title("🤖 AI Design Risk Prediction System")

# Description
st.markdown("""
This tool helps engineers evaluate structural design risk.

### Parameters:
- Length (meters)
- Load (kg)
- Material

👇 Enter values below:
""")

# Inputs in columns
col1, col2 = st.columns(2)

with col1:
    length = st.number_input("Length (meters)", min_value=0, value=10)

with col2:
    load = st.number_input("Load (kg)", min_value=0, value=100)

# Material selection
material = st.selectbox("Material", ["steel", "aluminum"])

# Button
if st.button("🚀 Predict Risk"):
    with st.spinner("Analyzing design..."):
        result = predict_risk(length, load, material)

    # Result section
    st.markdown("### 📊 Result")

    if result == "high":
        st.error("⚠️ High Risk! Consider safer design.")
    elif result == "medium":
        st.warning("⚡ Medium Risk. Review design.")
    else:
        st.success("✅ Safe Design")

    # Explanation section
    st.markdown("### 🔍 Explanation")

    if result == "high":
        st.write("High load or weaker material increases structural failure risk.")
    elif result == "medium":
        st.write("Moderate load — design should be reviewed.")
    else:
        st.write("Low load ensures safe design.")
