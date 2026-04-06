import streamlit as st
from model import predict_risk

st.title("AI Design Risk Prediction System")

st.write("Enter design parameters to predict risk level")

length = st.number_input("Length", min_value=0)
load = st.number_input("Load", min_value=0)
material = st.selectbox("Material", ["steel", "aluminum"])

if st.button("Predict Risk"):
    result = predict_risk(length, load, material)
    
    st.subheader(f"Predicted Risk: {result}")

    if result == "high":
        st.error("High risk! Consider safer design.")
    elif result == "medium":
        st.warning("Moderate risk. Review design.")
    else:
        st.success("Safe design.")
