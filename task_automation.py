
from datetime import datetime
from pathlib import Path
import json

# Get the folder containing this Python file.
PROJECT_FOLDER = Path(__file__).parent

# File where test results will be saved.
RESULTS_FILE = PROJECT_FOLDER / "test_cases.md"

# Prompt used to transform raw notes.
AUTOMATION_PROMPT = """
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
"""

# Three example inputs for testing.
TEST_CASES = {
    "1": {
        "name": "College Meeting",
        "input": (
            "Team meeting on Monday. Submit project report by Friday. "
            "Riya will prepare slides. Discussed website design."
        )
    },
    "2": {
        "name": "Class Notes",
        "input": (
            "Python uses variables to store values. "
            "Loops repeat instructions. Practice for and while loops "
            "before the next class."
        )
    },
    "3": {
        "name": "Event Planning",
        "input": (
            "College tech event next month. Book auditorium. "
            "Ask volunteers to register. Budget is not decided yet."
        )
    }
}


def show_menu():
    print("\n" + "=" * 42)
    print("       SMART NOTES FORMATTER")
    print("=" * 42)
    print("1. View automation prompt")
    print("2. View test examples")
    print("3. Save an AI test result")
    print("4. Exit")


def view_prompt():
    print("\n--- AUTOMATION PROMPT ---")
    print(AUTOMATION_PROMPT)
    print("\nCopy this prompt into ChatGPT to test it.")


def view_examples():
    print("\n--- TEST EXAMPLES ---")

    for number, case in TEST_CASES.items():
        print(f"\nExample {number}: {case['name']}")
        print("Input:", case["input"])


def save_result():
    print("\nChoose a test example: 1, 2, or 3")
    number = input("Your choice: ").strip()

    if number not in TEST_CASES:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    case = TEST_CASES[number]

    print("\n--- PROMPT TO USE IN CHATGPT ---")
    print(AUTOMATION_PROMPT)

    print("\n--- RAW NOTES INPUT ---")
    print(case["input"])

    print(
        "\nNow combine the prompt and raw notes in ChatGPT."
        "\nPaste the actual ChatGPT response below."
        "\nType END on a new line when finished."
    )

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    output = "\n".join(lines).strip()

    if not output:
        print("No response entered. Nothing was saved.")
        return

    observation = input(
        "\nWhat did you observe about this result? "
    ).strip()

    record = f"""
## Example {number}: {case['name']}

**Test date:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

### Input
{case['input']}

### Prompt Used
{AUTOMATION_PROMPT}

### Actual AI Output
{output}

### Observation
{observation if observation else "Observation not entered."}

---
"""

    with RESULTS_FILE.open("a", encoding="utf-8") as file:
        file.write(record)

    print(f"\nResult saved to: {RESULTS_FILE}")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_prompt()
        elif choice == "2":
            view_examples()
        elif choice == "3":
            save_result()
        elif choice == "4":
            print("Thank you for using Smart Notes Formatter!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()