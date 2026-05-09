# Elementary Chatbot for Customer Interaction

print("===================================")
print(" Welcome to Customer Support Bot ")
print("===================================")

print("\nType 'bye' to exit the chat.\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:

        print("Bot: Hello! How can I help you today?")

    # Product inquiry
    elif "product" in user:

        print("Bot: We provide laptops, mobiles, and accessories.")

    # Price inquiry
    elif "price" in user:

        print("Bot: Prices depend on the product model and brand.")

    # Delivery inquiry
    elif "delivery" in user:

        print("Bot: Delivery usually takes 3 to 5 business days.")

    # Payment inquiry
    elif "payment" in user:

        print("Bot: We accept UPI, Credit Card, Debit Card, and Net Banking.")

    # Contact inquiry
    elif "contact" in user:

        print("Bot: You can contact us at support@example.com")

    # Thanks response
    elif "thank" in user:

        print("Bot: You're welcome!")

    # Exit condition
    elif user == "bye":

        print("Bot: Thank you for visiting. Have a nice day!")
        break

    # Default response
    else:

        print("Bot: Sorry, I did not understand your query.")