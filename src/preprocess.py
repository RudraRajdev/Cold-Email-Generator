import json

def load_user_details(filename):
    """Load user details from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def preprocess_user_details(user_details):
    """Preprocess user details to extract key information."""
    # Example preprocessing steps
    skills = user_details.get('skills', [])
    experience = user_details.get('experience', '')
    past_companies = user_details.get('past_company', [])
    job_role = user_details.get('job_role', '')

    # Additional preprocessing could be applied here
    # For example, normalizing or removing unnecessary characters

    return {
        'skills': skills,
        'experience': experience,
        'past_companies': past_companies,
        'job_role': job_role
    }

def save_preprocessed_data(data, filename):
    """Save preprocessed data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Preprocessed data saved to {filename}")

def main():
    user_details = load_user_details('user_details.json')
    preprocessed_data = preprocess_user_details(user_details)
    save_preprocessed_data(preprocessed_data, 'preprocessed_data.json')

if __name__ == "__main__":
    main()
