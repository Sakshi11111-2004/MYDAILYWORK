import re

def chatbot_response(user_input):
    # Convert input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\bhello\b|\bhi\b|\bhey\b|\bgreetings\b|\bsup\b', user_input):
        return "Hello! How can I assist you today?"
    if re.search(r'\bGood Morning\b',user_input):
        return "Good Morning! How can I assist you today?"

    # Farewells
    elif re.search(r'\bbye\b|\bexit\b|\bquit\b|\bsee you\b|\btake care\b', user_input):
        return "Goodbye! Have a great day!"

    # Specific questions
    elif re.search(r'\bhow are you\b|\bhow\'s it going\b|\bhow are things\b', user_input):
        return "I'm just a bot, but I'm here to help you!"

    elif re.search(r'\bwhat\'s your name\b|\bwho are you\b', user_input):
        return "I'm a simple chatbot created to assist you!"

    elif re.search(r'\bwhat can you do\b|\bhow can you help\b', user_input):
        return "I can chat with you, answer simple questions, and keep you company!"

    elif re.search(r'\bweather\b|\bforecast\b', user_input):
        return "I can't check the weather, but it's always a good day to code!"

    elif re.search(r'\btime\b|\bcurrent time\b', user_input):
        return "I don't have a clock, but it's the perfect time to be productive!"

    # Default response for unrecognized input
    else:
        return "I'm not sure how to respond to that. Could you ask something else?"

def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if 'bye' in user_input.lower():
            break

if __name__ == "__main__":
    main()
