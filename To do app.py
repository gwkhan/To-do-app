# To-Do List Manager CLI Project

to_do = []

def load_tasks():
    try:
        with open("tasks.txt") as f:
            for line in f:
                to_do.append(line.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close()  # create empty file if missing

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in to_do:
            f.write(task + "\n")

def add_tasks():
    entries = input("Enter task(s), separated by commas: ")
    tasks = [t.strip() for t in entries.split(",") if t.strip()]
    if not tasks:
        print("❌ No valid tasks entered.")
        return
    to_do.extend(tasks)
    save_tasks()
    print("✅ Task(s) added.")

def view_tasks():
    if not to_do:
        print("📭 No tasks found.")
        return
    print("📋 Your Tasks:")
    for i, task in enumerate(to_do, start=1):
        print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if not to_do:
        return
    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(to_do):
            removed = to_do.pop(num - 1)
            save_tasks()
            print(f"🗑️ Removed: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

def main():
    load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("What do you want to do? (1-4): ").strip().lower()
        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()