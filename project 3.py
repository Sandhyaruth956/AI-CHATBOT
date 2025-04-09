import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'what is your name\?', ['I am an NLTK chatbot! What can I assist you with?']),
    (r'how are you\?', ['I am a bot, so I don’t have feelings, but I am here to help! How about you?']),
    (r'what can you do\?', [
        'I can answer your queries, help with information, and keep you company!',
        'I am here to assist you with any questions or tasks.'
    ]),
    (r'(.*) help (.*)', ['Of course! What do you need help with?', 'I’m here to help you. Please ask your question.']),
    (r'(.*) your purpose(.*)', ['My purpose is to assist and answer your questions!']),
    (r'(.*) (weather|news|time)', ['I cannot provide real-time updates yet, but feel free to ask other questions.']),
    (r'bye|exit', ['Goodbye! Have a great day!', 'See you soon!', 'Take care!']),
    (r'(.*)', ['I am sorry, I don’t understand that. Could you rephrase it?']),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get the chatbot's response
        response = chatbot.respond(user_input)
        
        # Default response if no match found
        if not response:
            response = "I’m not sure how to respond to that. Can you try asking in a different way?"
        
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
