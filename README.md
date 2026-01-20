Markdown

# 🎙️ AI Meeting Summarizer

An automated tool that transforms meeting recordings into structured, professional minutes. It uses **OpenAI Whisper** for high-accuracy speech-to-text and **CrewAI** with **Google Gemini 1.5 Flash** for intelligent summarization.

---

## 🚀 Features
* **Speech-to-Text:** Transcribes `.mp4` and `.mp3` files using OpenAI's Whisper (Base model).
* **AI Summarization:** Uses an AI Agent (CrewAI) to extract key insights, decisions, and action items.
* **Professional Formatting:** Outputs results in scannable Markdown format.
* **Custom Roles:** Designed with a "Meeting Minutes Specialist" persona for high-quality summaries.

---

## 🛠️ Tech Stack
* **Python:** Core programming language.
* **Whisper:** For local audio transcription.
* **CrewAI:** For orchestrating the AI agent workflow.
* **LangChain:** For seamless integration with Google Gemini.
* **Google Gemini 1.5 Flash:** The LLM used for intelligent processing.

---

## 📋 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-meeting-summarizer.git](https://github.com/YOUR_USERNAME/ai-meeting-summarizer.git)
cd ai-meeting-summarizer
2. Create Virtual Environment
Bash

python -m venv venv
source venv/Scripts/activate  # For Windows
3. Install Dependencies
Bash

pip install whisper crewai langchain-google-genai python-dotenv litellm
4. Setup Environment Variables
Create a .env file in the root directory and add your API key:

Code snippet

GEMINI_API_KEY=your_actual_gemini_api_key_here
📖 How to Use
Place your meeting recording (e.g., audio.mp4) in the project folder.

Open app.py and ensure the filename matches: AUDIO_FILE = "audio.mp4".

Run the application:

Bash

python app.py
The transcript and AI-generated summary will be saved as a .md file in the same folder.

🤖 Scalability & Future Improvements
Multilingual Support: Adding support for Hindi and other regional languages.

Speaker Diarization: Identifying who said what during the meeting.

Web Interface: Creating a Streamlit or Flask UI for easier file uploads.

Cloud Integration: Uploading summaries directly to Google Drive or Slack.

📜 License
This project is for educational/assignment purposes.
