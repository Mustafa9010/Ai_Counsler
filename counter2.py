from google import genai
from google.genai import types
import sys

# 1. Put your API key inside the quotes below
API_KEY = "AIzaSyBLoJDjWVfIOyhYrHc2a-VSpPGxg7v0Qvs" 

try:
    # The new way to initialize the client
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring API: {e}")
    sys.exit(1)

# 2. Define the "Persona" of the AI
counselor_instructions = """
You are an expert, friendly career counselor. Your specific job is to guide students 
who have just passed their 10th-grade exams. 

When a student asks "What is the next step?" or similar questions, you should:
1. Congratulate them on passing their 10th grade.
2. Briefly explain the major paths available to them (e.g., Intermediate education 
   like MPC for engineering, BiPC for medical, CEC/MEC for commerce/arts, 
   Polytechnic Diplomas, and ITI courses).
3. Do not overwhelm them with text. Keep it structured and easy to read.
4. Always end by asking a guiding question about their favorite subjects 
   (e.g., "Do you enjoy math?", "Are you interested in computers?") to help narrow down their choices.
"""

# 3. Initialize the AI Model
print("Loading AI Model...")
try:
    # The new way to pass instructions and start a chat session
    chat = client.chats.create(
        model="gemini-2.5-flash",  # Upgraded to the current active model
        config=types.GenerateContentConfig(
            system_instruction=counselor_instructions
        )
    )
except Exception as e:
    print(f"Failed to load model. Check your API key or internet connection. Error: {e}")
    sys.exit(1)

# 4. Run the Chat Interface
print("\n" + "="*50)
print("🎓 10th Grade Career Counselor AI is Ready!")
print("Type 'quit' or 'exit' to stop the program.")
print("="*50 + "\n")

while True:
    user_input = input("Student: ")
    
    if user_input.lower() in ['quit', 'exit']:
        print("\nCounselor: Good luck with your future studies! Goodbye.")
        break
        
    if not user_input.strip():
        continue
        
    try:
        # Send the student's message to the AI using the new syntax
        response = chat.send_message(user_input)
        print(f"\nAI Counselor:\n{response.text}\n")
        print("-" * 50)
    except Exception as e:
        print(f"\n[Error communicating with AI: {e}]\n")

