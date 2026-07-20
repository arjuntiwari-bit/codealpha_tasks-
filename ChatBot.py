
def chatbot():
    print("🤖 ChatBot: Hello! I am your simple chatbot.")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello" or user == "hi":
            print("ChatBot: Hi! How can I help you?")

        elif user == "how are you?" or user == "How are you?":
            print("ChatBot: I'm fine, thanks! How about you?")

        elif user == "i am fine" or user == "I am fine":
            print("ChatBot: That's great to hear!")

        elif user == "what is your name?" or user == "What is your name?":
            print("ChatBot: My name is Basic ChatBot.")

        elif user == "who created you?" or user == "Who created you?":
            print("ChatBot: I was created using Python.")

        elif user == "thank you" or user == "thanks":
            print("ChatBot: You're welcome!")

        elif user == "bye" or user == "Bye":
            print("ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")


chatbot()