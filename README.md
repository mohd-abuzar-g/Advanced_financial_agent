# Advanced Travel Agent
Advanced Travel Agent is an AI-powered travel planning application built with **Streamlit**, **OpenRouter (Gemini Flash)**, and **Serper.dev**.  
It generates full multi-day itineraries based on user preferences, travel style, and destination, including essential travel information and calendar integration.

---

🚀 Features
🧠 AI-Generated Itineraries
- Generates detailed day-by-day travel plans (1–14 days)  
- Supports travel styles: **Balanced, Luxury, Budget, Adventure**  
- Integrates weather, visa rules, and local tips  
- Uses **OpenRouter LLM models** for AI reasoning  
 🌍 Real-Time Search
- Integrates **Serper.dev** for fetching live travel info  
- Provides context on top attractions, weather forecasts, and visa requirements  
 📅 Calendar Integration
- Exports itinerary as **.ics file** for Google, Apple, or Outlook Calendar  
 🖥️ Modern UI
- Built with **Streamlit** for interactive, clean user experience  
- Sidebar inputs for arrival date, travel style, and search mode  
- Multi-chunk itinerary generation for flexible planning  

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Advanced_travel_agent.git
```

2. Navigate into the project folder:
```bash
cd Advanced_travel_agent
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

 ▶️ Usage

Run the app:

```bash
streamlit run Advanced_travel_agent.py
```
- Enter your **OpenRouter API Key** and **Serper.dev API Key** in the sidebar  
- Input **destination**, **number of days**, **travel style**, and **arrival date**  
- Click **Generate Plan**  
- Download the itinerary as a **.ics calendar file**  



🗂 Project Structure

```
Advanced_travel_agent/
│── Advanced_travel_agent.py       # Main Streamlit application
│── README.md                     # Project description
│── requirements.txt              # Python dependencies
```


 🔑 API Keys
OpenRouter API Key** – Required for AI reasoning  
Serper.dev API Key** – Required for live search  

**No keys are hardcoded in the repository** — safe to publish on GitHub.

---

 📄 License

This project is for educational and personal use.

