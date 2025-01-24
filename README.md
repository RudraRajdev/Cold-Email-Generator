Cold Email Generator

🌟 Overview

Cold Email Generator is a tool designed to create personalized cold emails by leveraging user-provided details such as skills, experience, and job roles. It uses modern NLP techniques to generate embeddings and extract insights for crafting impactful emails. Additionally, it provides a Streamlit Web App for a user-friendly interface.

🚀 Features

🌐 User Input Collection: Collects user details interactively, including skills, experience, and job roles.

⚡ Data Preprocessing: Processes and normalizes user-provided information for downstream tasks.

🔒 Integration with APIs: Utilizes the Groq API for generating meaningful email content.

🖥️ Streamlit Web App: A simple and interactive web interface for users to input details and generate cold emails.

🛠️ Technologies Used

Programming Languages: Python

Libraries: Hugging Face Transformers, PyTorch, JSON, Streamlit

APIs: Groq API, Gemini API

Tools: .env for managing API keys

📂 Project Structure

Cold_Email_Generator/
├── src/
│   ├── embadding.py         # Handles embedding generation using BERT
│   ├── preprocess.py        # Preprocesses user input details
│   ├── user_input.py        # Collects user input interactively
├── app.py                   # Streamlit web app for user interaction
├── .env                     # Environment variables for API keys
├── requirements.txt         # Dependencies for the project
└── README.md                # Project documentation

🚀 Getting Started

Prerequisites

Python 3.11

Required libraries: Install dependencies from requirements.txt using:
$pip install -r requirements.txt

Installation

# Clone the repository
$ git clone https://github.com/RudraRajdev/Cold-Email-Generator.git

# Navigate to the project directory
$ cd Cold-Email-Generator

# Install dependencies
$ pip install -r requirements.txt

Usage

Step 1: Set up environment variables

Create a .env file in the project directory with the following content:

GROQ_API_KEY=<your_groq_api_key>
GEMINI_API_URL=<your_gemini_api_url>

Step 2: Run the Streamlit Web App

Launch the web application using Streamlit:

$ streamlit run app.py

Step 3: Generate Emails

Open the web app in your browser (Streamlit will provide a link).

Enter your details, such as skills, experience, and job role.

Generate and view the personalized cold email.

🎯 Use Cases

📈 Personalized cold email generation for job applications

💼 Custom email creation for marketing or networking purposes

📸 Screenshots/Demo

(Include relevant screenshots or GIFs showcasing your project in action.)

📝 Contributing

We welcome contributions to this project! Follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature-branch).

Submit a pull request.

📜 License

This project is licensed under the MIT License.

🌐 Connect with Me

LinkedIn: www.linkedin.com/in/rudra-rajdev-b4b14b2b2

GitHub: RudraRajdev

Feel free to star ⭐ this repository if you found it useful!

