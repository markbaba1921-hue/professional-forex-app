import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import yfinance as yf

# Page configuration
st.set_page_config(
    page_title="PRO Forex Trader",
    page_icon="🎯",
    layout="wide"
)

st.title("🏛️ PROFESSIONAL FOREX TRADING APP")
st.markdown("**Institutional-Grade Market Analysis**")

class ProfessionalTradingEngine:
    def get_forex_data(self, symbol, period="5d", interval="15m"):
        """Get real forex data"""
        try:
            if '/' in symbol:
                symbol = symbol.replace('/', '') + '=X'
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period, interval=interval)
            return data
        except:
            return self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate realistic sample data"""
        dates = pd.date_range(end=datetime.now(), periods=100, freq='15min')
        prices = [1.1000]
        for i in range(1, 100):
            change = np.random.normal(0, 0.0005)
            prices.append(prices[-1] * (1 + change))
        
        return pd.DataFrame({
            'Open': [p * 0.9998 for p in prices],
            'High': [p * 1.0005 for p in prices],
            'Low': [p * 0.9995 for p in prices],
            'Close': prices,
            'Volume': np.random.randint(1000, 10000, 100)
        }, index=dates)
    
    def calculate_indicators(self, df):
        """Calculate technical indicators"""
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # Moving Averages
        df['MA_20'] = df['Close'].rolling(20).mean()
        df['MA_50'] = df['Close'].rolling(50).mean()
        
        return df
    
    def analyze_signals(self, df):
        """Generate trading signals"""
        if len(df) < 50:
            return "HOLD", 50
        
        current = df.iloc[-1]
        
        # RSI Signal
        rsi_signal = "BUY" if current['RSI'] < 30 else "SELL" if current['RSI'] > 70 else "HOLD"
        
        # MA Signal
        ma_signal = "BUY" if current['MA_20'] > current['MA_50'] else "SELL"
        
        # Determine final signal
        if rsi_signal == "BUY" and ma_signal == "BUY":
            return "STRONG_BUY", 85
        elif rsi_signal == "SELL" and ma_signal == "SELL":
            return "STRONG_SELL", 85
        elif rsi_signal == "BUY" or ma_signal == "BUY":
            return "BUY", 70
        elif rsi_signal == "SELL" or ma_signal == "SELL":
            return "SELL", 70
        else:
            return "HOLD", 50

# Initialize engine
engine = ProfessionalTradingEngine()

# Sidebar
st.sidebar.title("🎯 Trading Controls")
selected_pairs = st.sidebar.multiselect(
    "Currency Pairs",
    ['EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CHF', 'AUD/USD'],
    default=['EUR/USD', 'GBP/USD']
)

# Main content
if selected_pairs:
    for pair in selected_pairs:
        st.markdown(f"### 📊 {pair} - Professional Analysis")
        
        # Get data and analyze
        data = engine.get_forex_data(pair)
        data = engine.calculate_indicators(data)
        signal, confidence = engine.analyze_signals(data)
        
        # Display signal
        if signal == "STRONG_BUY":
            st.success(f"🚀 {signal} | Confidence: {confidence}%")
        elif signal == "BUY":
            st.info(f"📈 {signal} | Confidence: {confidence}%")
        elif signal == "STRONG_SELL":
            st.error(f"🔻 {signal} | Confidence: {confidence}%")
        elif signal == "SELL":
            st.warning(f"📉 {signal} | Confidence: {confidence}%")
        else:
            st.info(f"⚖️ {signal} | Confidence: {confidence}%")
        
        # Create chart
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                          vertical_spacing=0.1, subplot_titles=('Price', 'RSI'),
                          row_heights=[0.7, 0.3])
        
        # Price
        fig.add_trace(go.Candlestick(x=data.index, open=data['Open'],
                                    high=data['High'], low=data['Low'],
                                    close=data['Close'], name='Price'), row=1, col=1)
        
        # RSI
        fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], name='RSI'), row=2, col=1)
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
        
        fig.update_layout(height=600, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Trading info
        current_price = data['Close'].iloc[-1]
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Price", f"{current_price:.5f}")
            st.metric("RSI", f"{data['RSI'].iloc[-1]:.1f}")
        
        with col2:
            st.metric("Signal", signal)
            st.metric("Confidence", f"{confidence}%")
        
        with col3:
            st.metric("Trend", "Bullish" if data['MA_20'].iloc[-1] > data['MA_50'].iloc[-1] else "Bearish")
            st.metric("Volatility", "High" if data['Close'].std() > 0.001 else "Low")

st.markdown("---")
st.success("**PROFESSIONAL FOREX APP** - Real-time analysis with institutional-grade indicators")
