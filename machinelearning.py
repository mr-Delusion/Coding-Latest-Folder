import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "I am": "You are",
    "I was": "You were",
    "I": "You",
    "You are": "I am",
    "You were": "I was",
    "Your": "My",
    "You": "I",
    "My": "Your",
    "Me": "You",
    "We": "You",
}

pairs = [
    [
        r"Hi|Hello|Hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"What is your name?",
        ["I am a chatbot created to assist you."]
    ],
    [
        r"How are you?",
        ["I'm just a computer program, but thanks for asking! How can I help you today?"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm not sure where I am, but I'm here to help you!"]
    ],
    [
        r"How is the weather in (.*)?",
        ["I don't have real-time data, but you can check a weather website for that information."]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye! Have a great day!", "See you later!"]
    ]
]

def mychat():
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    mychat()    