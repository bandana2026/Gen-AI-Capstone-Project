conversation_memory = {
    "user_name": None,
    "last_ticket": None
}


import random
import re
from database import support_tickets


def classify_message(message):
    message = message.lower()


    if "thank" in message or "positive" in message or "good" in message:
        return "positive"

    elif "issue" in message or "problem" in message:
        return "negative"

    elif "ticket" in message:
        return "query"

    else:
        return "unknown"
    
def feedback_handler(category):
    customer_name = conversation_memory["user_name"] or "Customer"

    if category == "positive":
        return f"Thank you for your kind words, {customer_name}! We're delighted to assist you."

    elif category == "negative":
        ticket_number = str(random.randint(100000, 999999))
        conversation_memory["last_ticket"] = ticket_number
        return f"We apologize for the inconvenience. Ticket #{ticket_number} has been created. Our team will follow up shortly."


def query_handler(message):
    match = re.search(r"\d+", message)

    if match:
        ticket_number = match.group()

        if ticket_number in support_tickets:
            status = support_tickets[ticket_number]
            return f"Ticket #{ticket_number} status: {status}"
        else:
            return f"Sorry, Ticket #{ticket_number} was not found."

    return "Please provide a valid ticket number."

def smart_intro(message):
    if conversation_memory["user_name"] is None:
        words = message.split()
        if len(words) == 1:
            conversation_memory["user_name"] = words[0].capitalize()
            return f"Nice to meet you, {conversation_memory['user_name']}! How can I assist you today?"
    return None


def context_agent(message):
    lower_msg = message.lower()

    if "latest ticket" in lower_msg or "my ticket" in lower_msg:
        ticket = conversation_memory.get("last_ticket")

        if ticket:
            return f"Your most recent ticket number is #{ticket}."
        else:
            return "I don't see any recent ticket yet."

    return None



def router(message):
    intro = smart_intro(message)
    if intro:
        return intro
    
    context_reply = context_agent(message)
    if context_reply:
        return context_reply

    category = classify_message(message)

    if category in ["positive", "negative"]:
        return feedback_handler(category)

    elif category == "query":
        return query_handler(message)

    else:
        return "Sorry, I could not understand your request."

print("\n🤖 Banking Customer Support AI Agent Started")
print("Type 'exit' to stop the chat.\n")

while True:
    user_message = input("You: ")

  
    if user_message.lower() == "exit":
        print("🤖 Agent: Thank you for contacting support. Goodbye!")
        break


    response = router(user_message)
    print(f"🤖 Agent: {response}")



