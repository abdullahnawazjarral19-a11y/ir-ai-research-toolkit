
import csv

FIELDS = [
    "author",
    "year",
    "title",
    "main_argument",
    "methodology",
    "research_gap",
]

def add_research_entry():
    print("\nEnter Research Details\n")

    entry = {}

    for field in FIELDS:
        entry[field] = input(
            f"{field.replace('_', ' ').title()}: "
        ).strip()

    with open(
        "literature_review.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDS
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(entry)

    print("\nResearch entry saved successfully!")

def main():
    print("IR-AI Research Organizer")
    print("-----------------------")

    while True:
        print("\n1. Add research entry")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_research_entry()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
