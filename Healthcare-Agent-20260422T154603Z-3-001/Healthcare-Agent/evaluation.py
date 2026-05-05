def execute_tools(plan):

    print("\n⚙ Executing Tools:\n")

    from tools import (
        retrieve_medical_history,
        find_nephrologist,
        book_appointment,
        search_treatment
    )

    print(retrieve_medical_history("father"))

    doctor = find_nephrologist()
    print(doctor)

    print(book_appointment("father", "Dr. Sharma"))

    print(search_treatment())