import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Forex Pro", layout="wide")

st.title("💰 FOREX TRADING SIGNALS")
st.write("Professional Market Analysis")

# Simple trading logic
def get_signal(pair):
    signals = {
        'EUR/USD': ('BUY', 85),
        'GBP/USD': ('BUY', 78), 
        'USD/JPY': ('SELL', 72),
        'USD/CHF': ('HOLD', 65),
        'AUD/USD': ('BUY', 81)
    }
    return signals.get(pair, ('HOLD', 50))

# Sidebar
st.sidebar.title("Controls")
pairs = st.sidebar.multiselect(
    "Select Pairs:",
    ['EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CHF', 'AUD/USD'],
    default=['EUR/USD', 'GBP/USD']
)

# Main content
if pairs:
    for pair in pairs:
        st.subheader(f"📈 {pair}")
        
        signal, confidence = get_signal(pair)
        
        # Display signal
        if signal == 'BUY':
            st.success(f"🚀 **{signal}** | Confidence: {confidence}%")
        elif signal == 'SELL':
            st.error(f"🔻 **{signal}** | Confidence: {confidence}%")
        else:
            st.info(f"⚖️ **{signal}** | Confidence: {confidence}%")
        
        # Price data
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Price", "1.0850" if 'EUR' in pair else "1.2650")
            st.metric("Today's Change", "+0.25%")
        
        with col2:
            st.metric("Stop Loss", "1.0800" if 'EUR' in pair else "1.2600")
            st.metric("Take Profit", "1.0950" if 'EUR' in pair else "1.2750")
        
        with col3:
            st.metric("Risk/Reward", "1:2.5")
            st.metric("Position Size", "1.2 lots")
        
        st.progress(confidence)

st.success("✅ App running successfully!")
