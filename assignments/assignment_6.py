import os
import re

# Folder to store notes
NOTES_DIR = "usernotes"

# Predefined sentiment words
positive_words = ["happy", "good", "excellent", "great", "fantastic", "love", "awesome"]
negative_words = ["sad", "bad", "terrible", "hate", "horrible", "angry", "poor"]

# Ensure notes folder exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

# Function to analyze sentiment of a note
def analyze_sentiment(text):
    text = text.lower()
    pos_count = sum(len(re.findall(r'\b' + word + r'\b', text)) for word in positive_words)
    neg_count = sum(len(re.findall(r'\b' + word + r'\b', text)) for word in negative_words)
    
    print(f"Positive words count: {pos_count}")
    print(f"Negative words count: {neg_count}")
    
    if pos_count > neg_count:
        print("Overall Sentiment: Positive ")
    elif neg_count > pos_count:
        print("Overall Sentiment: Negative ")
    else:
        print("Overall Sentiment: Neutral ")

# Function to read and analyze notes
def read_notes():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes found.")
        return
    
    print("\nAvailable Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    
    choice = input("\nEnter note number to analyze or 'all' to analyze all notes: ").strip()
    
    if choice.lower() == "all":
        for note in notes:
            print(f"\n--- Analyzing {note} ---")
            with open(os.path.join(NOTES_DIR, note), 'r') as file:
                content = file.read()
                print(f"Content:\n{content}\n")
                analyze_sentiment(content)
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(notes):
                note = notes[index]
                print(f"\n--- Analyzing {note} ---")
                with open(os.path.join(NOTES_DIR, note), 'r') as file:
                    content = file.read()
                    print(f"Content:\n{content}\n")
                    analyze_sentiment(content)
            else:
                print("Invalid note number.")
        except ValueError:
            print("Invalid input.")

# Function to create a new note
def create_note():
    filename = input("Enter note filename (with .txt): ").strip()
    filepath = os.path.join(NOTES_DIR, filename)
    
    if os.path.exists(filepath):
        print("Note already exists!")
        return
    
    content = input("Enter note content:\n")
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"Note '{filename}' created successfully!")

# Function to modify an existing note
def modify_note():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("No notes found.")
        return
    
    print("\nAvailable Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    
    try:
        choice = int(input("\nEnter note number to modify: ")) - 1
        if 0 <= choice < len(notes):
            note = notes[choice]
            filepath = os.path.join(NOTES_DIR, note)
            with open(filepath, 'r') as file:
                content = file.read()
            print(f"Current Content:\n{content}\n")
            new_content = input("Enter new content:\n")
            with open(filepath, 'w') as file:
                file.write(new_content)
            print(f"Note '{note}' updated successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input.")

# Main program loop
def main():
    while True:
        print("\n===== Intelligent Notes Management System =====")
        print("1. Read & Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            read_notes()
        elif choice == "2":
            create_note()
        elif choice == "3":
            modify_note()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
