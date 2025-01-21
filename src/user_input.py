import json

def get_user_input():
    """Collect user input for skills, experience, past companies, job role, and company name."""
    skills = input("Enter your skills (comma-separated): ")
    experience = input("Enter your experience in years (numeric only): ")
    
    # Check if experience is numeric and 1 year or more
    try:
        experience_years = int(experience)
        if experience_years >= 1:
            past_companies = input("Enter past companies (comma-separated): ")
        else:
            past_companies = []  # Default to empty list if experience is less than 1 year
    except ValueError:
        print("Invalid experience input. Please enter a numeric value.")
        return None

    job_role = input("Enter the job role you are applying for: ")
    company_name = input("Enter the company name where you are applying: ")

    user_details = {
        'skills': [skill.strip() for skill in skills.split(',')],
        'experience': experience.strip(),
        'past_companies': [company.strip() for company in past_companies.split(',')] if past_companies else [],
        'job_role': job_role.strip(),
        'company_name': company_name.strip()
    }

    return user_details

def save_user_details(user_details, filename):
    """Save user input details to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(user_details, file, indent=4)
        print(f"User details saved to {filename}")
    except IOError as e:
        print(f"Error saving user details: {e}")

def main():
    user_details = get_user_input()
    if user_details:
        save_user_details(user_details, 'user_details.json')

if __name__ == "__main__":
    main()
