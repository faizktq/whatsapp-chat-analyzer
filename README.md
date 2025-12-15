# 📱 WhatsApp Chat Analyzer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)

A comprehensive data analysis tool built with **Python** and **Streamlit** that transforms your exported WhatsApp chat files (`.txt`) into insightful visualizations.

---

## 📊 Features

### 1. **Top Statistics**
   - Total Messages, Words, Media Shared, and Links Shared.
   
### 2. **Timeline Analysis**
   - **Monthly Timeline:** See how activity trends over time.
   - **Daily Timeline:** Track daily message volumes.

### 3. **Activity Maps**
   - **Most Busy Day:** Identifies which day of the week your group is most active.
   - **Most Busy Month:** Identifies the most active month of the year.
   - **Weekly Heatmap:** A visual grid showing the busiest hours of the week.

### 4. **Text Analysis**
   - **Word Cloud:** A visual representation of the most frequently used words.
   - **Most Common Words:** Bar chart of top words (filtering out stop words).
   - **Hinglish Support:** Custom stop words list to handle "Hinglish" chat terms (e.g., *hai, mein, kya*).

### 5. **Emoji Analysis**
   - Interactive Pie Chart showing the distribution of emojis used.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Visualization:** Plotly, Matplotlib, Seaborn
* **NLP:** NLTK, URLExtract, WordCloud

---

## 🚀 How to Run Locally

Follow these steps to set up the project on your local machine.

### Prerequisites
* Python 3.7+ installed

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/faizktq/whatsapp-chat-analyzer.git](https://github.com/faizktq/whatsapp-chat-analyzer.git)
    cd whatsapp-chat-analyzer
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

```text
├── app.py               # Main Streamlit application
├── preprocessor.py      # Data cleaning and date parsing logic
├── helper.py            # Analysis functions (Stats, WordCloud, etc.)
├── requirements.txt     # List of dependencies
├── stop_words.txt       # Custom list of English & Hinglish stop words
└── README.md            # Project documentation