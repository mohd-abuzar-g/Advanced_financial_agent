# Advanced Financial Agent

Advanced Financial Agent is an AI-powered system designed for **real-time stock analysis, market sentiment detection, and financial insights**.  
It uses live financial data and AI reasoning to generate professional reports and recommendations for any stock symbol.

---

## 🚀 Features

### 📈 Real-Time Stock Analysis
- Fetches current stock data including price, market cap, PE ratios, 52-week high, dividend yield, and sector  
- Detects market mood as **Bullish** or **Bearish** using AI reasoning  

### 🤖 AI-Powered Financial Reports
- Uses **OpenRouter-compatible AI models** (DeepSeek, Gemini Flash) for professional interpretation  
- Generates executive summary, bull case, bear case, and final verdict  
- Supports multiple stock tickers in one query  

### 📰 News Integration
- Fetches recent news using **NewsAPI** (optional) or DuckDuckGo  
- Provides context for AI analysis, helping detect market trends  

### 🗨️ Interactive Query System
- Users can input any stock ticker and get **structured, real-time insights**  
- Fully conversational AI-driven analysis  

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Advanced_financial_agent.git
```

2. Navigate into the project folder:
```bash
cd Advanced_financial_agent
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
streamlit run app.py
```

- Enter your **OpenRouter API Key** in the sidebar  
- Optionally, enter a **NewsAPI Key** for enhanced news-based insights  
- Enter one or more **stock tickers** (e.g., NVDA, TSLA)  
- Click **Start Analysis** to get AI-generated reports  

---

## 🗂 Project Structure

```
Advanced_financial_agent/
│── finance_agent.py        # Main Streamlit application
│── README.md               # Project description
│── requirements.txt        # Python dependencies
```

---

## 🔑 API Keys

- **OpenRouter API Key** – Required for AI reasoning  
- **NewsAPI Key** (optional) – For fetching news headlines; if not provided, the system uses DuckDuckGo  

**No API keys are hardcoded** — safe to publish on GitHub.

---

## 📄 License

This project is for educational and personal use.
