import time
def chatbot_response(message):
    time.sleep(1)
    message = message.lower().strip()

    if message in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "Hello Mansi! How can I help you today?"

    elif message in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye! Have a great day."
    
    elif mesaage in["how its going"]:
        return "Nice, What about you"

    elif message.endswith("?"):
        return "That's a good question. Let me think about it."


    else:
        return "I'm not sure how to respond to that."

def main():
    print("Welcome to Simple AI Chatbot!")

    user=input("Enter your name:")
  
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
