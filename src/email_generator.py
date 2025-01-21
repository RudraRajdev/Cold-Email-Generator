import json
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv('GROQ_API_KEY')

# Check if API key is loaded properly
if not api_key:
    raise ValueError("API key is missing. Please check your .env file.")

# Initialize the ChatGroq instance
llm = ChatGroq(
    temperature=0,
    groq_api_key=api_key,
    model_name="Gemma2-9b-it"
)

def generate_cold_email(job_role, skills, experience, past_companies):
    """Generate a personalized cold email using ChatGroq."""
    prompt = (
        f"Generate a personalized cold email for a job role '{job_role}' with the following details:\n"
        f"Skills: {', '.join(skills)}\n"
        f"Experience: {experience}\n"
        f"Past Companies: {', '.join(past_companies)}\n"
        f"The email should be professional and tailored to the job role."
    )

    try:
        # Generate the response
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        print(f"Error communicating with ChatGroq: {e}")
        return None

def load_user_details(filename):
    """Load user details from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading user details: {e}")
        return None

def main():
    # Load user details
    user_details = load_user_details('preprocessed_data.json')
    
    if not user_details:
        print("User details could not be loaded. Exiting.")
        return

    # Generate cold email
    email = generate_cold_email(
        user_details.get('job_role', 'Unknown Role'),
        user_details.get('skills', []),
        user_details.get('experience', 'Unknown Experience'),
        user_details.get('past_companies', [])
    )

    if email:
        print("Generated Cold Email:")
        print(email)
    else:
        print("Failed to generate the cold email.")

if __name__ == "__main__":
    main()
