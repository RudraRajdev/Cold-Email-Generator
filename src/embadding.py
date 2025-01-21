from transformers import AutoTokenizer, AutoModel
import torch
import json

def initialize_model(model_name='bert-base-uncased'):
    """Load the Hugging Face model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model

def get_embedding(text, tokenizer, model):
    """Generate embedding for a given text using Hugging Face model."""
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Take the mean of the last hidden states to get the embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding

def load_preprocessed_data(filename):
    """Load preprocessed user details from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

def save_embeddings_to_file(user_details, filename, tokenizer, model):
    """Save embeddings for user details to a JSON file."""
    embeddings = {}
    for skill in user_details['skills']:
        embedding = get_embedding(skill, tokenizer, model)
        embeddings[skill] = embedding.tolist()  # Convert numpy array to list for JSON serialization

    with open(filename, 'w') as file:
        json.dump(embeddings, file, indent=4)
    print(f"Embeddings saved to {filename}")

def main():
    # Initialize Hugging Face model and tokenizer
    tokenizer, model = initialize_model('bert-base-uncased')
    
    # Load preprocessed user details
    preprocessed_data = load_preprocessed_data('preprocessed_data.json')
    
    # Save embeddings to file
    save_embeddings_to_file(preprocessed_data, 'user_embeddings.json', tokenizer, model)

if __name__ == "__main__":
    main()
