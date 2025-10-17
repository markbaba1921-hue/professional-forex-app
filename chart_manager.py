import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class ProfessionalChartManager:
    def create_trading_chart(self, df, trading_plan=None):
        """Create professional trading chart with indicators"""
        fig = make_subplots(
            rows=4, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.03,
            subplot_titles=('Price Action', 'RSI', 'MACD', 'Volume'),
            row_heights=[0.5, 0.15, 0.15, 0.2],
            specs=[[{"secondary_y": False}], [{"secondary_y": False}], 
                   [{"secondary_y": False}], [{"secondary_y": False}]]
        )
        
        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='Price'
        ), row=1, col=1)
        
        # Bollinger Bands
        if 'BB_Upper' in df.columns:
            fig.add_trace(go.Scatter(
                x=df.index, y=df['BB_Upper'],
                line=dict(color='rgba(255, 0, 0, 0.7)', width=1),
                name='BB Upper'
            ), row=1, col=1)
            
            fig.add_trace(go.Scatter(
                x=df.index, y=df['BB_Lower'],
                line=dict(color='rgba(0, 255, 0, 0.7)', width=1),
                fill='tonexty',
                name='BB Lower'
            ), row=1, col=1)
        
        # Trading levels
        if trading_plan:
            fig.add_hline(y=trading_plan['entry_price'], line_dash="dash", 
                         line_color="blue", annotation_text="ENTRY", row=1, col=1)
            fig.add_hline(y=trading_plan['stop_loss'], line_dash="dash", 
                         line_color="red", annotation_text="SL", row=1, col=1)
            fig.add_hline(y=trading_plan['take_profit_1'], line_dash="dash", 
                         line_color="green", annotation_text="TP1", row=1, col=1)
            fig.add_hline(y=trading_plan['take_profit_2'], line_dash="dash", 
                         line_color="darkgreen", annotation_text="TP2", row=1, col=1)
        
        # RSI
        if 'RSI' in df.columns:
            fig.add_trace(go.Scatter(
                x=df.index, y=df['RSI'],
                line=dict(color='purple', width=2),
                name='RSI'
            ), row=2, col=1)
            
            # RSI levels
            fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
            fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
            fig.add_hline(y=50, line_dash="dot", line_color="gray", row=2, col=1)
        
        # MACD
        if 'MACD' in df.columns and 'MACD_Signal' in df.columns:
            fig.add_trace(go.Scatter(
                x=df.index, y=df['MACD'],
                line=dict(color='blue', width=2),
                name='MACD'
            ), row=3, col=1)
            
            fig.add_trace(go.Scatter(
                x=df.index, y=df['MACD_Signal'],
                line=dict(color='red', width=2),
                name='MACD Signal'
            ), row=3, col=1)
            
            # MACD Histogram
            colors = ['green' if val >= 0 else 'red' for val in (df['MACD'] - df['MACD_Signal'])]
            fig.add_trace(go.Bar(
                x=df.index,
                y=df['MACD'] - df['MACD_Signal'],
                marker_color=colors,
                name='MACD Hist'
            ), row=3, col=1)
        
        # Volume
        if 'Volume' in df.columns:
            colors = ['green' if df['Close'].iloc[i] >= df['Open'].iloc[i] 
                     else 'red' for i in range(len(df))]
            
            fig.add_trace(go.Bar(
                x=df.index,
                y=df['Volume'],
                marker_color=colors,
                name='Volume'
            ), row=4, col=1)
        
        fig.update_layout(
            height=800,
            title="Professional Forex Analysis",
            xaxis_rangeslider_visible=False,
            showlegend=True
        )
        
        return fig
