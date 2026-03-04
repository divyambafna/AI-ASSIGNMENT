def turing_test():
    """
    A simple simulation of a Turing Test interaction.
    The program asks the user questions and provides responses.
    """
    print("--- Turing Test Simulation ---")
    print("Initiating conversation... Type 'quit' to end.\n")

    # A simple dictionary-based response system
    responses = {
        "hello": "Hello! How are you feeling today?",
        "how are you": "I am functioning within normal parameters. And you?",
        "what is your name": "I don't have a name, but you can call me Simulation.",
        "are you a computer": "That depends on how you define 'computer'. I think, therefore I am... processing.",
        "what is 2+2": "It is 4. Why are you testing my basic arithmetic?",
    }

    while True:
        user_input = input("User: ").lower().strip()

        if user_input == 'quit':
            print("Simulation: Goodbye.")
            break

        # Check for keywords in the user input
        found = False
        for key in responses:
            if key in user_input:
                print(f"Simulation: {responses[key]}")
                found = True
                break
        
        if not found:
            print("Simulation: That is an interesting perspective. Tell me more.")

if __name__ == "__main__":
    turing_test()
