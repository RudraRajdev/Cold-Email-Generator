import streamlit as st
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
    st.error("API key is missing. Please check your .env file.")
    st.stop()

# Initialize the ChatGroq instance
llm = ChatGroq(
    temperature=0,
    groq_api_key=api_key,
    model_name="llama-3.1-70b-versatile"
)

def generate_cold_email(job_role, company_name, skills, experience, past_companies):
    """Generate a personalized cold email using ChatGroq."""
    prompt = (
        f"Generate a personalized cold email for a job role '{job_role}' at '{company_name}' with the following details:\n"
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
        st.error(f"Error communicating with ChatGroq: {e}")
        return None

def save_user_details(user_details, filename):
    """Save user input details to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(user_details, file, indent=4)
    st.success(f"User details saved to {filename}")

# Streamlit app interface
st.title("Cold Email Generator")

st.header("Enter Your Details")
job_role = st.text_input("Job Role")
company_name = st.text_input("Company Name")
skills = st.text_area("Skills (comma-separated)").split(',')
experience = st.number_input("Years of Experience", min_value=0)
if experience > 0:
    past_companies = st.text_area("Past Companies (comma-separated)").split(',')
else:
    past_companies = []

# Button to generate the cold email
if st.button("Generate Cold Email"):
    if not job_role or not company_name:
        st.error("Please provide both Job Role and Company Name.")
    else:
        email = generate_cold_email(job_role, company_name, skills, f"{experience} years", past_companies)
        if email:
            st.subheader("Generated Cold Email:")
            st.write(email)
            
           
