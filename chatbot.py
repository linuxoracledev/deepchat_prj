import random

def get_response(user_input):
    # A simple function to generate chatbot responses based on user input
    user_input = user_input.lower()

    if 'hello' in user_input:
        return "Hi there! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a chatbot, but I'm doing fine! How about you?"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Get chatbot response
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
