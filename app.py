import streamlit as st

st.title("💰 Forex Trading Signals")
st.write("This app is working!")

# Simple forex pairs
pairs = ["EUR/USD", "GBP/USD", "USD/JPY"]

selected_pair = st.selectbox("Choose a pair:", pairs)

if selected_pair == "EUR/USD":
    st.success("BUY Signal - Confidence: 85%")
elif selected_pair == "GBP/USD":
    st.info("HOLD Signal - Confidence: 65%")  
else:
    st.error("SELL Signal - Confidence: 75%")

st.metric("Current Price", "1.0850", "+0.0020")
st.metric("Daily Range", "1.0800 - 1.0900")

st.success("✅ App is running successfully!")
