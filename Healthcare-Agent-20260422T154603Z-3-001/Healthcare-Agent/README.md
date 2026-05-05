# Healthcare Planning Agent

## Project Overview

The Healthcare Planning Agent is a modular AI-inspired system designed to assist users in managing medical-related tasks. 

It accepts a medical request from the user and:

- Breaks the request into structured planning steps
- Executes healthcare-related tools
- Simulates appointment booking and treatment research

This project demonstrates agent architecture, modular design, and tool orchestration.

---

## Problem Statement

Managing medical appointments and treatment research can be overwhelming for patients and families.

This project aims to:

- Automate healthcare task planning
- Provide structured breakdown of medical requests
- Simulate execution of healthcare assistance tools

Example:
User request:  
"Book nephrologist for my father and summarize kidney treatment"

The agent:
- Retrieves medical history
- Finds nephrologist
- Books appointment
- Searches treatments
- Summarizes options

---

## Architecture

The project follows a modular agent-based architecture:

```
User Input → Planner Agent → Plan Output → Tool Execution → Final Output
```
The planner module generates structured tasks from user input.
The execution module interprets the plan and activates relevant healthcare tools.

### File Structure

- `app.py` → Main execution file
- `planner_agent.py` → Task planning logic
- `tools.py` → Healthcare tool implementations
- `evaluation.py` → Tool execution controller
- `memory.py` → (Optional memory module)
- `rag_pipeline.py` → (Optional RAG integration)

---

## Technologies Used

- Python 3.10+
- Modular Function Design
- Agent-based workflow
- Simulated Tool Execution
- VS Code

(Optional Version Includes)
- LangChain
- OpenAI API
- dotenv

---

## How to Run the Project

### Step 1: Open Terminal inside project folder

### Step 2: Run the application

```
python app.py
```

### Step 3: Enter medical request when prompted

Example input:

```
Book nephrologist for my father and summarize kidney treatment
```

---

## Sample Output

```
Patient: father

Tasks:
1. Retrieve medical history
2. Find nephrologist availability
3. Book appointment
4. Search latest kidney treatments
5. Summarize treatment methods

Executing Tools:

Medical history for father: Chronic Kidney Disease, Hypertension
Available nephrologist: Dr. Sharma at 4 PM
Appointment booked for father with Dr. Sharma
Latest kidney treatments: Dialysis optimization, Transplant support, AI monitoring
```

---

## Key Features

- Modular architecture
- Clear separation of planning and execution
- Simulated healthcare tool ecosystem
- Easy to extend for real API integration
- Beginner-friendly AI agent design

---
## Design Principles

Separation of concerns (planning vs execution)

Modular architecture

Expandable tool framework

API-ready structure for real-world integration

## Future Improvements

- Integrate real hospital booking API
- Add patient memory tracking
- Implement Retrieval-Augmented Generation (RAG)
- Add evaluation metrics
- Deploy as web application

---

## Author

Bandana S  
Healthcare Planning Agent Project  
2026