# 🎙️ Speech-to-Summary Bot (AI Meeting Summarizer)

This project is an AI-powered tool that converts meeting audio recordings into a clean, structured, and professional summary.  
It uses **OpenAI Whisper** for speech-to-text transcription and **CrewAI with Google Gemini** for intelligent summarization.

---

## 📂 Project Structure

```
speech-to-summary-bot/
├── venv/                 # Python virtual environment
├── app.py                # Main application file
├── audio.mp4             # Input meeting audio file
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (API key)
└── README.md             # Project documentation
```

---

## 🚀 Features

- **Speech-to-Text Conversion**
  - Converts `.mp4` audio files into text
  - Uses OpenAI Whisper (Base model)

- **AI-Based Summarization**
  - Generates:
    - Meeting title
    - Key discussion points
    - Important decisions
    - Action items
  - Uses CrewAI with a *Meeting Minutes Specialist* agent

- **Clean Output**
  - Structured and readable summary
  - Displayed directly in the terminal
  - Easy to save or reuse as meeting minutes

- **Error Handling**
  - Handles transcription and summarization errors safely

---

## 🛠️ Tech Stack

- **Python 3.12**
- **OpenAI Whisper** – Audio transcription
- **CrewAI** – AI agent orchestration
- **LangChain Google GenAI** – LLM integration
- **Google Gemini** – Intelligent summarization
- **python-dotenv** – Environment variable management

---

## 📦 Dependencies (requirements.txt)

```
whisper
crewai
langchain-google-genai
python-dotenv
litellm
```

Install dependencies using:

```
pip install -r requirements.txt
```

---

## ⚙️ Setup Instructions

### Clone Repository
```
git clone https://github.com/Abhishek10075/speech-to-summary-bot.git
cd speech-to-summary-bot
```

### Create & Activate Virtual Environment (Windows)
```
python -m venv venv
source venv/Scripts/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Setup Environment Variables
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

⚠️ Never upload `.env` to GitHub

---

## ▶️ How to Run

1. Put audio file in project folder:
```
audio.mp4
```

2. Check filename in `app.py`:
```
AUDIO_FILE = "audio.mp4"
```

3. Run:
```
python app.py
```

4. Output:
- Transcript (Whisper)
- Structured summary (AI)
- Printed in terminal

---

## 🤖 AI Agent

- Role: Meeting Minutes Specialist
- Task:
  - Analyze transcript
  - Generate structured summary
- Output:
  - Meeting Title
  - Key Discussion Points
  - Important Decisions
  - Action Items

---

## 🔮 Future Improvements

- Multilingual support (Hindi, regional languages)
- Speaker diarization
- Export summary as `.md` / `.pdf`
- Streamlit / Flask UI
- Cloud integration (Google Drive, Slack)

---

## 📜 License

Educational and learning purposes only.
