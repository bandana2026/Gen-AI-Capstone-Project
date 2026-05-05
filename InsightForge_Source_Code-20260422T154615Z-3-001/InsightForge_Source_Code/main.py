from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma3:4b")

system_prompt = """
You are InsightForge AI, a senior Business Intelligence consultant.
Give analytical, structured, business-focused responses.
Be clear, professional, and insight-driven.
"""

conversation_history = system_prompt

print("InsightForge AI Ready. Type your question. Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

         

    if user_input.lower().startswith("/analyst"):
        mode_prompt = "\n[ROLE: Senior Data Analyst]"
        user_input = user_input.replace("/analyst", "").strip()

    elif user_input.lower().startswith("/strategy"):
        mode_prompt = "\n[ROLE: Business Strategy Consultant]"
        user_input = user_input.replace("/strategy", "").strip()

    elif user_input.lower().startswith("/kpi"):
        mode_prompt = "\n[ROLE: KPI & Performance Expert]"
        user_input = user_input.replace("/kpi", "").strip()

    else:
        mode_prompt = "\n[ROLE: Business Intelligence Assistant]"

    conversation_history += f"{mode_prompt}\nUser: {user_input}"

    response = llm.invoke(conversation_history)

    conversation_history += f"\nAI: {response}"

    print("AI:", response)
