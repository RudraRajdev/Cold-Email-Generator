import streamlit as st
from langchain_groq import ChatGroq

# Set your Groq API key here
api_key = ""  # Put your Groq API key

# Check if API key is loaded properly
if not api_key:
    st.error("API key is missing. Please provide a valid API key.")
    st.stop()

# Initialize the ChatGroq instance
llm = ChatGroq(
    temperature=0,
    api_key=api_key,
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
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        st.error(f"Error communicating with ChatGroq: {e}")
        return None

def main():
    st.title("Cold Email Generator")
    st.write("Generate personalized cold emails based on job details.")

    job_role = st.text_input("Job Role", "")
    skills = st.text_area("Skills (comma-separated)", "").split(', ')
    experience = st.text_input("Experience (e.g., 3 years)", "")
    past_companies = st.text_area("Past Companies (comma-separated)", "").split(', ')

    if st.button("Generate Email"):
        email = generate_cold_email(job_role, skills, experience, past_companies)
        if email:
            st.subheader("Generated Cold Email")
            st.text_area("", email, height=200)
        else:
            st.error("Failed to generate the cold email.")

if __name__ == "__main__":
    main()
