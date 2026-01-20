import os
import whisper
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from datetime import datetime

# 1. Environment variables load karein (.env file se)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ Error: GEMINI_API_KEY nahi mili! .env file check karein.")
    exit()

class MeetingSummarizerAI:
    def __init__(self):
        # 2. Gemini LLM Setup (Explicitly using LangChain)
        # Temperature 0.2 rakha hai taaki summary factual rahe
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GEMINI_API_KEY,
            temperature=0.2
        )
        
        # 3. Agent Definition
        # 'function_calling_llm' add kiya hai taaki LiteLLM error na aaye
        self.agent = Agent(
            role='Meeting Minutes Specialist',
            goal='Extract key insights, decisions, and action items from transcripts.',
            backstory="""You are a professional executive assistant known for 
            your ability to summarize long meetings into concise, actionable points.""",
            llm=self.llm,
            function_calling_llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def generate_summary(self, transcript_text):
        # 4. Task Definition
        task = Task(
            description=f"""Analyze the following transcript and provide a structured summary:
            
            TRANSCRIPT:
            {transcript_text}
            
            STRUCTURE TO FOLLOW:
            - **Meeting Title/Goal** (Based on context)
            - **Key Discussion Points** (Bullet points)
            - **Important Decisions** (What was agreed upon)
            - **Action Items** (Who needs to do what)
            """,
            expected_output="A well-structured meeting summary in Markdown format.",
            agent=self.agent
        )
        
        # 5. Crew Execution
        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        return result.raw # .raw se clean string milti hai

def main():
    # File check
    AUDIO_FILE = "audio.mp4"
    if not os.path.exists(AUDIO_FILE):
        print(f"❌ Error: {AUDIO_FILE} file folder mein nahi hai!")
        return

    try:
        # STEP 1: Transcription (Using Whisper)
        print("\n--- Step 1: Transcribing Audio (Whisper) ---")
        model = whisper.load_model("base")
        result = model.transcribe(AUDIO_FILE, fp16=False)
        transcript = result['text']
        print(f"✅ Transcription Complete! ({len(transcript)} characters)")

        # STEP 2: AI Summary (Using CrewAI + Gemini)
        print("\n--- Step 2: Generating AI Summary (CrewAI) ---")
        summarizer = MeetingSummarizerAI()
        final_summary = summarizer.generate_summary(transcript)
        
        # STEP 3: Saving the Result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"summary_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_summary)
            
        print(f"\n✅ SUCCESS! Summary saved in: {filename}")
        print("\n--- FINAL SUMMARY ---\n")
        print(final_summary)

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()