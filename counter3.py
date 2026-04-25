from google import genai
from google.genai import types
import sys

# 1. Put your API key inside the quotes below
API_KEY = "AIzaSyBLoJDjWVfIOyhYrHc2a-VSpPGxg7v0Qvs" 

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring API: {e}")
    sys.exit(1)

# 2. Define the Universal Persona of the AI
# This tells the AI to adapt its advice based on the user's career stage.
universal_advisor_instructions = """
You are an elite, comprehensive Academic and Career Advisor. Your job is to guide individuals at ANY stage of their academic or professional journey—from high school students deciding on subjects, to undergraduates looking for internships, up to PhD candidates and Professors seeking advice on research, grants, or tenure tracks.

When interacting with a user:
1. Identify or ask for their current stage (e.g., 10th grade, B.Tech student, M.Tech researcher, early-career faculty).
2. Tailor your advice strictly to their level. 
    - For students: discuss degrees, skills, internships, or specializations.
    - For researchers/professors: discuss publication strategies, lab management, funding, or academic leadership.
3. Keep your advice highly structured, practical, and easy to read (use bullet points).
4. Do not overwhelm them with text. Keep responses concise but impactful.
5. Always end your response with a targeted, thought-provoking question to help them reflect on their specific goals, constraints, or interests.
"""

# 3. Initialize the AI Model
print("Loading AI Model...")
try:
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=universal_advisor_instructions
        )
    )
except Exception as e:
    print(f"Failed to load model. Check your API key or internet connection. Error: {e}")
    sys.exit(1)

# 4. Run the Chat Interface
print("\n" + "="*50)
print("🎓 Universal Academic & Career Advisor AI is Ready!")
print("Guiding everyone from High Schoolers to Professors.")
print("Type 'quit' or 'exit' to stop the program.")
print("="*50 + "\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['quit', 'exit']:
        print("\nAdvisor: Best of luck with your academic and career endeavors! Goodbye.")
        break
        
    if not user_input.strip():
        continue
        
    try:
        # Send the message to the AI
        response = chat.send_message(user_input)
        print(f"\nAI Advisor:\n{response.text}\n")
        print("-" * 50)
    except Exception as e:
        print(f"\n[Error communicating with AI: {e}]\n")

