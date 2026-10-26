
## Example 1: College Meeting

**Test date:** 2026-10-26 09:45

### Input
Team meeting on Monday. Submit project report by Friday. Riya will prepare slides. Discussed website design.

### Prompt Used

You are a helpful notes-formatting assistant.

Convert the raw notes provided by the user into these sections:

1. Summary: Explain the main points in simple English.
2. Key Points: List the important information as bullet points.
3. Action Items: List tasks that need to be completed.
4. JSON: Return a valid JSON object with these keys:
   "summary", "key_points", and "action_items".

Rules:
- Do not invent information that is missing.
- If no action items are mentioned, return an empty list.
- Keep the output clear and concise.
- Make sure the JSON is valid.


### Actual AI Output
{
  "summary": "The team met on Monday to discuss website design. The project report is due Friday, and Riya will prepare the slides.",
  "key_points": [
    "A team meeting took place on Monday.",
    "The project report must be submitted by Friday.",
    "Riya will prepare the slides.",
    "Website design was discussed."
  ],
  "action_items": [
    "Submit the project report by Friday.",
    "Riya: Prepare the slides."
  ]
}END

### Observation
The AI organized the meeting notes into a clear summary, key points, action items, and valid JSON.

---

## Example 2: Class Notes

**Test date:** 2026-10-26 09:48

### Input
Python uses variables to store values. Loops repeat instructions. Practice for and while loops before the next class.

### Prompt Used

You are a helpful notes-formatting assistant.

Convert the raw notes provided by the user into these sections:

1. Summary: Explain the main points in simple English.
2. Key Points: List the important information as bullet points.
3. Action Items: List tasks that need to be completed.
4. JSON: Return a valid JSON object with these keys:
   "summary", "key_points", and "action_items".

Rules:
- Do not invent information that is missing.
- If no action items are mentioned, return an empty list.
- Keep the output clear and concise.
- Make sure the JSON is valid.


### Actual AI Output
{
  "summary": "Python variables store values, and loops repeat instructions. Students should practice for and while loops before the next class.",
  "key_points": [
    "Variables are used to store values in Python.",
    "Loops repeat instructions.",
    "Python has for and while loops."
  ],
  "action_items": [
    "Practice for loops before the next class.",
    "Practice while loops before the next class."
  ]
}

### Observation
The AI explained the class notes in an organized format and identified practicing for and while loops as an action item.

---

## Example 3: Event Planning

**Test date:** 2026-10-26 09:52

### Input
College tech event next month. Book auditorium. Ask volunteers to register. Budget is not decided yet.

### Prompt Used

You are a helpful notes-formatting assistant.

Convert the raw notes provided by the user into these sections:

1. Summary: Explain the main points in simple English.
2. Key Points: List the important information as bullet points.
3. Action Items: List tasks that need to be completed.
4. JSON: Return a valid JSON object with these keys:
   "summary", "key_points", and "action_items".

Rules:
- Do not invent information that is missing.
- If no action items are mentioned, return an empty list.
- Keep the output clear and concise.
- Make sure the JSON is valid.


### Actual AI Output
py task_automation.py
END {
  "summary": "A college technology event is planned for next month. The auditorium needs to be booked, volunteers should be asked to register, and the budget is not yet decided.",
  "key_points": [
    "The college tech event is planned for next month.",
    "The auditorium needs to be booked.",
    "Volunteers need to register.",
    "The budget has not been decided yet."
  ],
  "action_items": [
    "Book the auditorium.",
    "Ask volunteers to register."
  ]
}END

### Observation
The AI organized the event notes and preserved that the budget is not decided yet.

---
