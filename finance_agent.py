import streamlit as st
import yfinance as yf
import pandas as pd
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
import requests
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(page_title="AI Finance Agent", layout="wide", page_icon="💰")
st.title("💰 AI Finance Agent (Pro Version)")
st.caption("Professional stock analysis using Live Data + AI Reasoning.")

# --- SIDEBAR: Credentials ---
with st.sidebar:
    st.header("⚙️ Configuration")

    # 1. The Brain
    model_key = st.text_input("OpenRouter API Key", type="password")

    # 2. The Model Selector
    model_choice = st.selectbox(
        "Select AI Model",
        [
            "deepseek/deepseek-r1",            
            "google/gemini-2.0-flash-001",     
            "openai/gpt-4o"                    
        ]
    )

    # 3. News Config
    st.divider()
    news_api_key = st.text_input("NewsAPI Key (Optional)", type="password", help="Get free key at newsapi.org")
    st.info("ℹ️ If no NewsAPI key is provided, the agent will use DuckDuckGo.")

# --- USER INPUT ---
stock_input = st.text_input("Enter Stock Ticker(s)", placeholder="e.g., NVDA, BTC-USD, TSLA")

# --- MAIN LOGIC ---
if st.button("🚀 Start Analysis", type="primary"):
    if not model_key:
        st.error("❌ Please enter your OpenRouter API Key in the sidebar to proceed.")
        st.stop()

    if not stock_input:
        st.warning("⚠️ Please enter at least one stock ticker.")
        st.stop()

    # Split tickers and clean whitespace
    tickers = [s.strip().upper() for s in stock_input.split(",") if s.strip()]

    # --- 1. SETUP AI AGENT ---
    try:
        model_engine = OpenRouter(id=model_choice, api_key=model_key)
        finance_agent = Agent(
            name="FinanceAnalyst",
            model=model_engine,
            tools=[DuckDuckGoTools()],
            instructions=[
                "You are a Senior Wall Street Analyst.",
                "Given the financial data and news provided, write a professional report.",
                "Structure: Executive Summary -> Bull Case -> Bear Case -> Final Verdict.",
                "Be skeptical and cite specific numbers from the provided data.",
            ],
            markdown=True
        )
    except Exception as e:
        st.error(f"Error setting up AI Agent: {e}")
        st.stop()

    # --- 2. ANALYZE EACH TICKER ---
    for ticker in tickers:
        # 2026 FIX: Using a Container ensures Company A isn't overwritten by Company B
        with st.container():
            st.divider()
            st.header(f"📈 Analysis for: {ticker}")

            # A. Get Real-time Data
            with st.status(f"🔍 Fetching data for {ticker}...", expanded=False) as status:
                try:
                    stock = yf.Ticker(ticker)
                    info = stock.info

                    stock_metrics = {
                        "Current Price": str(info.get("currentPrice", "N/A")),
                        "Market Cap": str(info.get("marketCap", "N/A")),
                        "PE Ratio (Trailing)": str(info.get("trailingPE", "N/A")),
                        "Forward PE": str(info.get("forwardPE", "N/A")),
                        "52-Week High": str(info.get("fiftyTwoWeekHigh", "N/A")),
                        "Dividend Yield": str(info.get("dividendYield", "N/A")),
                        "Sector": str(info.get("sector", "N/A"))
                    }
                    status.write("✅ Stock data received")
                except Exception as e:
                    st.error(f"Failed to fetch data for {ticker}: {e}")
                    stock_metrics = {}

                # B. Get News
                latest_news = []
                if news_api_key:
                    try:
                        url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={news_api_key}&pageSize=3&language=en"
                        response = requests.get(url).json()
                        articles = response.get("articles", [])
                        for art in articles:
                            pub_date = art.get("publishedAt", "")[:10]
                            latest_news.append(f"- {pub_date}: {art['title']} (Source: {art['source']['name']})")
                        status.write("✅ NewsAPI data received")
                    except Exception as e:
                        status.write(f"⚠️ NewsAPI error: {e}")

                status.update(label=f"Data for {ticker} complete!", state="complete", expanded=False)

            # C. Display Data Visually in Columns
            col1, col2 = st.columns([1, 2])

            with col1:
                st.subheader("📊 Key Metrics")
                # Table Header Fix: Metric and Value
                df = pd.DataFrame(list(stock_metrics.items()), columns=["Metric", "Value"])
                # 2026 Syntax Fix: width='stretch'
                st.dataframe(df, hide_index=True, width='stretch')

            with col2:
                st.subheader("🤖 AI Analyst Report")

                news_text = "\n".join(latest_news)
                full_prompt = f"""
                Analyze the stock symbol: {ticker}.
                Data: {stock_metrics}
                News: {news_text}
                
                Provide Bull vs Bear cases and a Final Verdict.
                """

                # Unique placeholder for the current ticker
                response_placeholder = st.empty()
                full_text = ""

                try:
                    # Stream the output for Company A completely before moving to Company B
                    for chunk in finance_agent.run(full_prompt, stream=True):
                        if hasattr(chunk, 'content') and chunk.content:
                            full_text += chunk.content
                            response_placeholder.markdown(full_text)
                except Exception as e:
                    st.error(f"AI Generation Error: {e}")
