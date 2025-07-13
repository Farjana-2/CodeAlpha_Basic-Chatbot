def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot.")
    print("Type something to talk with me. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  
        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thank you! How about you?")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break 
        else:
            print("🤖 Chatbot: I'm sorry, I don't understand that.")
chatbot()
