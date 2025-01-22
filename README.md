AvaBot Chatbot with Emojis
Description
AvaBot is an enhanced text-based chatbot that interacts with users in a natural and engaging way. It utilizes various natural language processing (NLP) techniques and features to provide meaningful and delightful conversations.

Features
Natural Language Processing: Utilizes NLTK (Natural Language Toolkit) for tokenization and lemmatization to preprocess user inputs for better pattern matching.

Sentiment Analysis: Basic sentiment analysis to determine the tone of user inputs and respond accordingly.

Personalized Responses: Includes specific responses such as recognizing the user's name when asked "Do you know me?".

Engaging Emojis: Adds suitable emojis to responses to make interactions more engaging and human-like.

Pattern Matching: Uses regular expressions to match user inputs with predefined patterns and respond accordingly.

Reflections: Implements reflections to make responses more natural and conversational.

Libraries and Frameworks Used
NLTK (Natural Language Toolkit): For tokenization, lemmatization, and basic NLP tasks.

nltk.tokenize.word_tokenize(): Tokenizes the user input into words.

nltk.stem.WordNetLemmatizer(): Lemmatizes words to their base form.

nltk.chat.util.Chat: A utility from NLTK to handle pattern matching and responses.

Random Library: To select random responses from predefined lists.

Re (Regular Expressions) Library: For matching user input patterns.

Code Overview
Initialization: Downloads necessary NLTK data for tokenization and lemmatization.

Sentiment Analysis Function: Analyzes the sentiment of user input to provide appropriate responses.

Preprocessing Function: Converts user input to lowercase, tokenizes it, and lemmatizes the tokens.

Pattern and Response Definition: Defines patterns and corresponding responses for the chatbot.

Main Chatbot Function: Processes user input, matches it with predefined patterns, performs sentiment analysis, and generates responses with added emojis.

Main Loop: Continuously takes user input, processes it, and provides responses until the user types 'bye'.

Specialities
Personalized Interaction: AvaBot recognizes the user and responds with a personalized message, making the interaction feel more special.

Emotional Engagement: Using emojis, AvaBot adds emotional context to its responses, making the conversation more lively and engaging.

Versatile Responses: AvaBot can handle a variety of inputs and provide meaningful responses, including answering questions, providing help, telling jokes, and more.

User-Friendly Design: AvaBot is designed to be user-friendly, with clear instructions and a smooth conversational flow.

Example Interactions
Greeting: "Hello! How can I help you today? 😊"

Asking for Name: "My name is AvaBot. Nice to meet you! 🤖"

Recognizing User: "Yes! You are Bibi Hamida Pir, who has programmed me. It's wonderful to chat with you! 😊"

Sentiment Response:

Positive: "I'm glad to hear that! 😊"

Negative: "I'm sorry to hear that. If there's anything I can do to help, let me know. 🙁"

Joke: "Why don’t scientists trust atoms? Because they make up everything! 😂"
