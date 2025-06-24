# 📧 Cold Email Generator

An AI-powered web app that scrapes job descriptions from any career page, extracts key info using LLMs, and generates personalized cold emails based on your Microsoft portfolio.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cold-email-generator.streamlit.app)

---

## 📂 Project Structure
  ```
   Cold Email Generator/
   │
   ├── App/
   │   ├── main.py         # Streamlit app entry point
   │   ├── chains.py       # Handles LLM prompts (job extraction + email writing)
   │   ├── portfolio.py    # Loads and queries portfolio links
   │   ├── utils.py        # Cleans scraped HTML text
   │
   ├── requirements.txt    # Python dependencies
   ├── .gitignore          # Git ignore rules
   ├── .env                # API keys (not pushed to GitHub)
   ├── README.md           # Project docs
   ```


---

## ⚙️ Features

- 🌐 Scrape any job posting URL
- 🧠 Extracts roles, skills, and descriptions with **LLaMA 3.1 via Groq**
- 📩 Generates cold outreach emails as a **Microsoft SWE Intern**
- 🔗 Matches portfolio links based on job requirements
- 🧹 Cleans messy text using regex + BeautifulSoup

---

## 🛠️ Tech Stack

- **LangChain**
- **Groq LLM (LLaMA 3.1 8B)**
- **ChromaDB**
- **Streamlit**
- **BeautifulSoup**
- Python 3.10+

---

## 🔧 Setup Instructions

1. **Clone the Repo**

   ```bash
   git clone https://github.com/developer-krish/cold-email-generator.git
   cd cold-email-generator
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
3. **Create a .env File**

   ```bash
   GROQ_API_KEY=your_groq_api_key_here
4. **Run the App**

   ```bash
   streamlit run App/main.py

## 📎 Example Use Case
  Input: A job posting URL from any company
  Output: A cold email tailored to that job, using your Microsoft experience and portfolio links

## 🙋‍♂️ Author
  Krish — @developer-krish
