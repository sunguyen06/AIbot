import modules.calendar as calendar_module
import modules.tasks as task_module
import modules.nlp as nlp_module

def main():
    print("Welcome to Smart Productivity AI!")
    print("Commands: 'show events', 'add task', 'sync calendar', 'exit'")

    while True:
        # Get user input
        command = input("Enter a command: ").lower()

        # Handle commands
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "show events":
            print(calendar_module.get_google_calendar_events())
        elif command.startswith("add task"):
            # Extract task name if provided in the command
            task_name = command.replace("add task", "").strip()
            if not task_name:
                # Prompt for task name if not provided
                task_name = input("Enter the task name: ").strip()
            if not task_name:  # Validate that task_name is not empty
                print("Task name cannot be empty. Please try again.")
                continue
            due_date = input("Enter the due date (YYYY-MM-DD) or press Enter to skip: ").strip()
            print(task_module.add_todoist_task(task_name, due_date or None))
        elif command == "sync calendar":
            print(calendar_module.sync_calendar_to_todoist())
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

