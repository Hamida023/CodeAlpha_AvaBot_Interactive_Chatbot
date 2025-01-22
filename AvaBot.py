import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a function to analyze sentiment (basic example)
def analyze_sentiment(user_input):
    positive_words = ["good", "great", "fine", "happy", "awesome"]
    negative_words = ["bad", "sad", "unhappy", "terrible", "not good"]
    
    for word in positive_words:
        if word in user_input:
            return "positive"
    
    for word in negative_words:
        if word in user_input:
            return "negative"
    
    return "neutral"

# Define a function to preprocess user input
def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)

# Define a function for the enhanced chatbot
def enhanced_chatbot(user_input):
    # Preprocess the user input
    user_input = preprocess_input(user_input)

    # Define some patterns and responses
    patterns = {
        r'hello|hi|hey': ["Hello! How can I help you today?😊", "Hi there! What can I do for you?😃", "Hey! How's it going? 🙌"],
        r'how are you': ["I'm doing well, thank you for asking! How about you?😊", "I'm great, thanks! How are you doing?😃"],
        r'what is your name\??|who are you\??|your name\??': ["My name is AvaBot. Nice to meet you! 🤖", "I am AvaBot, your friendly chatbot!😊"],
        r'do you know me': ["Yes! You are Bibi Hamida Pir, who has programmed me. It's wonderful to chat with you!😊"],
        r'bye|goodbye': ["Goodbye! Have a great day!👋", "See you later! Take care!😊"],
        r'thank you|thanks': ["You're welcome! Anything else I can help with?😊", "No problem! Need anything else?😃"],
        r'weather': ["I'm sorry, I don't have access to real-time weather information.🌦️", "I can't provide weather updates, but you can check a weather app!🌤️"],
        r'help': ["I can answer simple questions. Try asking me about my name or how I'm doing!😊", "I'm here to help! Ask me anything.🤗"],
        r'how can you help me': ["I can chat with you, answer simple questions, and provide basic information!😊", "I'm here to assist with any questions or information you need!🤓"],
        r'tell me a joke': ["Why don’t scientists trust atoms? Because they make up everything!😂", "Why was the math book sad? Because it had too many problems.😅"]
    }

    # Check for matches and return appropriate response
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input):
            return random.choice(responses)

    # Sentiment analysis response
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "I'm glad to hear that!😊"
    elif sentiment == "negative":
        return "I'm sorry to hear that. If there's anything I can do to help, let me know. 🙁"
    
    # If no match is found, return a default response
    return "I'm not sure how to respond to that. Can you try rephrasing or asking something else? 🤔"

# Main loop for the chatbot
print("AvaBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("AvaBot: Goodbye!👋")
        break
    response = enhanced_chatbot(user_input)
    print("AvaBot:", response)
