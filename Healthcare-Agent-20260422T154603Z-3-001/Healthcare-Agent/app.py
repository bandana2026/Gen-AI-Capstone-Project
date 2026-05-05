from planner_agent import plan_tasks
from tools import retrieve_medical_history, find_nephrologist, book_appointment, search_treatment


def run_agent(user_query):

    print("\n🧠 Planner Output:\n")
    plan = plan_tasks(user_query)
    print(plan)

    print("\n⚙ Executing Tools:\n")

    
    if "Patient:" in plan:
        patient = plan.split("Patient:")[1].split("\n")[0].strip()
    else:
        patient = "father"

    print(retrieve_medical_history(patient))

    doctor = find_nephrologist()
    print(doctor)

    print(book_appointment(patient, "Dr. Sharma"))

    print(search_treatment())


if __name__ == "__main__":
    user_input = input("Enter medical request: ")
    run_agent(user_input)