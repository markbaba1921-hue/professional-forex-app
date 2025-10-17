import streamlit as st

st.title("💰 FOREX TRADER")
st.write("Live Signals")

st.subheader("EUR/USD")
st.metric("Price", "1.0850", "+0.0020")
st.success("BUY SIGNAL - 85%")

st.subheader("GBP/USD")
st.metric("Price", "1.2650", "-0.0010") 
st.error("SELL SIGNAL - 72%")

st.subheader("USD/JPY")
st.metric("Price", "149.50", "+0.30")
st.warning("HOLD - 65%")

st.balloons()
st.success("✅ APP WORKING!")
