def chatbot():
    print(" I'm ChatBot. What's your name?")
    name = input("You: ")

    print(f"Nice to meet you, {name}! How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if any(keyword in user_input for keyword in ["bank account", "statement", "transactions"]):
            print("ChatBot: Please let me know your account type?")
        elif "savings" in user_input:
            print("ChatBot: Okay! Let me know your 12-digit account number")
        elif "123456789121" in user_input:
            print("ChatBot: I have mailed you the details")
            break
        else:
            print("ChatBot: Sorry, I didn't understand that.")

# Call the chatbot function to start the conversation
chatbot()


 