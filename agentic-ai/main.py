from agent import Agent

if __name__ == "__main__":
    agent = Agent()

    print("🔹 Agentic CLI started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        result = agent.process(user_input)
        print("Agent:", result)